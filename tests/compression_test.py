"""Compressed responses for the sync (urllib3) and async (aiohttp) clients.

urllib3 does not send Accept-Encoding on its own, so before
scripts/generate.sh added it the sync client received every response
uncompressed: 10-60x more bytes for large index pages. aiohttp sends the
header by default. Both clients must also decode what comes back.

The header is injected after generation, so a future regeneration could drop
it without any other test noticing.
"""

import asyncio
import gzip
import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest

import vulncheck_sdk
import vulncheck_sdk.aio as vcaio

BODY = json.dumps({"data": [{"id": f"CVE-2024-{i:05d}", "description": "example"} for i in range(2000)]}).encode()

PROXY_ENV_VARS = (
    "HTTP_PROXY",
    "HTTPS_PROXY",
    "NO_PROXY",
    "ALL_PROXY",
    "http_proxy",
    "https_proxy",
    "no_proxy",
    "all_proxy",
)


class CompressingServer:
    """Serves BODY gzip-encoded when the client asks for gzip, and records what it was asked."""

    def __init__(self):
        self.requests = []
        outer = self

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                accept = self.headers.get("Accept-Encoding", "")
                outer.requests.append(accept)
                payload, encoding = BODY, None
                if "gzip" in accept:
                    payload, encoding = gzip.compress(BODY), "gzip"
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                if encoding:
                    self.send_header("Content-Encoding", encoding)
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)

            def log_message(self, *args):
                pass

        self._server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        threading.Thread(target=self._server.serve_forever, daemon=True).start()
        self.url = f"http://127.0.0.1:{self._server.server_address[1]}"

    def close(self):
        self._server.shutdown()
        self._server.server_close()


@pytest.fixture
def server(monkeypatch):
    for var in PROXY_ENV_VARS:
        monkeypatch.delenv(var, raising=False)
    s = CompressingServer()
    yield s
    s.close()


def test_sync_client_requests_and_decodes_compressed_responses(server):
    configuration = vulncheck_sdk.Configuration(host=server.url)
    with vulncheck_sdk.ApiClient(configuration) as api_client:
        assert "gzip" in api_client.default_headers["Accept-Encoding"]

        response = api_client.call_api(*api_client.param_serialize(method="GET", resource_path="/v3/index/example"))

        assert response.status == 200
        assert response.read() == BODY
    assert "gzip" in server.requests[0]


def test_async_client_requests_and_decodes_compressed_responses(server):
    async def fetch():
        configuration = vcaio.Configuration(host=server.url)
        async with vcaio.ApiClient(configuration) as api_client:
            response = await api_client.call_api(*api_client.param_serialize(method="GET", resource_path="/v3/index/example"))
            return response.status, await response.read()

    status, body = asyncio.run(fetch())

    assert status == 200
    assert body == BODY
    assert "gzip" in server.requests[0]
