"""Proxy environment handling for the sync (urllib3) client.

openapi-generator 7.24.0 taught the generated Configuration to read
HTTP(S)_PROXY / NO_PROXY from the environment, and rest.py to honour the
NO_PROXY bypass. Before that, Configuration.proxy was always None and the
SDK was unusable from behind a corporate proxy.

Both halves matter. Adopting a proxy *without* the bypass would silently
reroute all VulnCheck traffic for anyone who has HTTPS_PROXY set for
unrelated tooling, so these are pinned together.

Nothing else in the suite covers this, and a future regeneration could
drop it without any other test noticing.
"""

import os
import select
import socket
import threading

import pytest

import vulncheck_sdk

API_TOKEN = os.environ["VULNCHECK_API_TOKEN"]
API_HOST = "https://api.vulncheck.com"
API_HOSTNAME = "api.vulncheck.com"

# Proxy-related vars are read at Configuration() construction, so every one
# of them has to be cleared or the ambient environment leaks into the result.
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


class RecordingProxy:
    """Minimal HTTP CONNECT proxy that records what it is asked to tunnel."""

    def __init__(self):
        self._server = socket.socket()
        self._server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._server.bind(("127.0.0.1", 0))
        self._server.listen(16)
        self.port = self._server.getsockname()[1]
        self.requests = []
        self._stop = threading.Event()
        self._thread = threading.Thread(target=self._serve, daemon=True)
        self._thread.start()

    @property
    def url(self):
        return f"http://127.0.0.1:{self.port}"

    def _serve(self):
        while not self._stop.is_set():
            try:
                self._server.settimeout(0.5)
                client, _ = self._server.accept()
            except (socket.timeout, OSError):
                continue
            threading.Thread(
                target=self._handle, args=(client,), daemon=True
            ).start()

    def _handle(self, client):
        try:
            request = b""
            while b"\r\n\r\n" not in request:
                chunk = client.recv(4096)
                if not chunk:
                    return
                request += chunk

            request_line = request.split(b"\r\n")[0].decode(errors="replace")
            self.requests.append(request_line)

            verb, _, rest = request_line.partition(" ")
            if verb != "CONNECT":
                client.sendall(b"HTTP/1.1 501 Not Implemented\r\n\r\n")
                return

            target = rest.split(" ")[0]
            host, _, port = target.partition(":")
            upstream = socket.create_connection((host, int(port or 443)), timeout=10)
            client.sendall(b"HTTP/1.1 200 Connection Established\r\n\r\n")
            self._tunnel(client, upstream)
        except Exception:
            pass
        finally:
            _close(client)

    @staticmethod
    def _tunnel(a, b):
        try:
            while True:
                readable, _, _ = select.select([a, b], [], [], 10)
                if not readable:
                    return
                for source in readable:
                    data = source.recv(8192)
                    if not data:
                        return
                    (b if source is a else a).sendall(data)
        finally:
            _close(b)

    def shutdown(self):
        self._stop.set()
        self._thread.join(timeout=5)
        _close(self._server)


def _close(sock):
    try:
        sock.close()
    except Exception:
        pass


@pytest.fixture
def proxy():
    server = RecordingProxy()
    yield server
    server.shutdown()


@pytest.fixture
def clean_proxy_env(monkeypatch):
    for name in PROXY_ENV_VARS:
        monkeypatch.delenv(name, raising=False)


def _call_api():
    """Make one real request and return whether it succeeded."""
    config = vulncheck_sdk.Configuration(host=API_HOST)
    config.api_key["Bearer"] = API_TOKEN
    with vulncheck_sdk.ApiClient(config) as api_client:
        pool_manager = type(api_client.rest_client.pool_manager).__name__
        response = vulncheck_sdk.IndicesApi(api_client).index_exploits_get(limit=1)
        return config, pool_manager, response


def test_https_proxy_is_adopted_from_environment(proxy, clean_proxy_env, monkeypatch):
    monkeypatch.setenv("HTTPS_PROXY", proxy.url)

    config, pool_manager, response = _call_api()

    assert config.proxy == proxy.url
    assert pool_manager == "ProxyManager"
    assert response is not None
    assert any(
        line.startswith(f"CONNECT {API_HOSTNAME}:443") for line in proxy.requests
    ), f"expected the request to be tunnelled, proxy saw: {proxy.requests}"


def test_no_proxy_bypasses_the_proxy(proxy, clean_proxy_env, monkeypatch):
    monkeypatch.setenv("HTTPS_PROXY", proxy.url)
    monkeypatch.setenv("NO_PROXY", API_HOSTNAME)

    config, pool_manager, response = _call_api()

    assert config.no_proxy == API_HOSTNAME
    assert pool_manager == "PoolManager"
    assert response is not None
    assert proxy.requests == [], (
        f"NO_PROXY should have bypassed the proxy, but it saw: {proxy.requests}"
    )


def test_unrelated_no_proxy_entry_does_not_bypass(proxy, clean_proxy_env, monkeypatch):
    """A NO_PROXY that doesn't match the API host must not disable proxying."""
    monkeypatch.setenv("HTTPS_PROXY", proxy.url)
    monkeypatch.setenv("NO_PROXY", "example.com,10.0.0.0/8")

    _, pool_manager, response = _call_api()

    assert pool_manager == "ProxyManager"
    assert response is not None
    assert any(
        line.startswith(f"CONNECT {API_HOSTNAME}:443") for line in proxy.requests
    ), f"expected the request to be tunnelled, proxy saw: {proxy.requests}"
