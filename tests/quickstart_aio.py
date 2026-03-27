import asyncio
import json
import os
import aiohttp
import vulncheck_sdk.aio as vcaio

# Configuration
TOKEN = os.environ.get("VULNCHECK_API_TOKEN")

configuration = vcaio.Configuration()
configuration.api_key["Bearer"] = TOKEN
configuration.ignore_operation_servers = True


async def run_vulnerability_checks():
    # Use 'async with' to manage the ApiClient connection pool
    async with vcaio.ApiClient(configuration) as api_client:
        endpoints_client = vcaio.EndpointsApi(api_client)
        indices_client = vcaio.IndicesApi(api_client)
        # --- PURL Search ---
        # 'await' the coroutine to get results
        purl_response = await endpoints_client.purl_get("pkg:hex/coherence@0.1.2")
        if purl_response.data:
            print(f"PURL CVEs: {purl_response.data.cves}")

        # --- CPE Search ---
        cpe = "cpe:/a:microsoft:internet_explorer:8.0.6001:beta"
        # 'await' the coroutine to get results
        cpe_response = await endpoints_client.cpe_get(cpe)
        print(f"CPE Results for {cpe}:")
        for cve in cpe_response.data:
            print(f" - {cve}")

        # --- Index Query (NVD2) ---
        # 'await' the coroutine to get results
        nvd_response = await indices_client.index_vulncheck_nvd2_get(
            cve="CVE-2019-19781"
        )
        print(f"NVD2 Data: {nvd_response.data}")

        # --- Download Backup (Async) ---
        index_name = "initial-access"
        # 'await' the coroutine to get raw response bytes
        raw = await endpoints_client.backup_index_get_without_preload_content(index_name)
        response_data = json.loads(await raw.read())

        if response_data.get("data"):
            download_url = response_data["data"][0]["url"]
            file_path = f"{index_name}.zip"

            print(f"Downloading backup from {download_url}...")
            # Use aiohttp (already in your environment) for async download
            async with aiohttp.ClientSession() as session:
                async with session.get(download_url) as resp:
                    if resp.status == 200:
                        # 'await' the coroutine to get results
                        content = await resp.read()
                        with open(file_path, "wb") as f:
                            f.write(content)
                        print(f"Saved backup to {file_path}")


if __name__ == "__main__":
    # Entry point to start the event loop
    asyncio.run(run_vulnerability_checks())
