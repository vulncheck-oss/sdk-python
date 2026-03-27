import asyncio
import json
import os
import urllib.request
import vulncheck_sdk.aio as vcaio

# Configuration
TOKEN = os.environ.get("VULNCHECK_API_TOKEN")

configuration = vcaio.Configuration()
configuration.api_key["Bearer"] = TOKEN
configuration.ignore_operation_servers = True


def download_sync(url, file_path):
    """
    Standard synchronous download using urllib.request.
    This runs in a separate thread to avoid blocking the event loop.
    """
    with urllib.request.urlopen(url) as response:
        with open(file_path, "wb") as file:
            file.write(response.read())


async def main():
    # Use 'async with' to manage the connection life-cycle
    async with vcaio.ApiClient(configuration) as api_client:
        backup_client = vcaio.BackupApi(api_client)
        index = "initial-access"

        # 'await' the coroutine to get the raw response bytes
        raw = await backup_client.backup_index_get_without_preload_content(index)
        response_data = json.loads(await raw.read())
        download_url = response_data["data"][0]["url"]

        file_path = f"{index}.zip"

        print(f"Downloading {index} via urllib (offloaded to thread)...")

        # Use asyncio.to_thread to run the blocking call safely
        await asyncio.to_thread(download_sync, download_url, file_path)

        print(f"Successfully saved to {file_path}")


if __name__ == "__main__":
    asyncio.run(main())
