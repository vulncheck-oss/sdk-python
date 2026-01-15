import asyncio
import os
import requests
import vulncheck_sdk.aio as vcaio

# Configuration
DEFAULT_HOST = "https://api.vulncheck.com"
DEFAULT_API = DEFAULT_HOST + "/v3"
TOKEN = os.environ.get("VULNCHECK_API_TOKEN")

configuration = vcaio.Configuration(host=DEFAULT_API)
configuration.api_key["Bearer"] = TOKEN


def download_sync(url, file_path):
    """
    Standard synchronous download using requests.
    This runs in a separate thread to avoid blocking the event loop.
    """
    response = requests.get(url)
    response.raise_for_status()
    with open(file_path, "wb") as file:
        file.write(response.content)


async def main():
    # Use 'async with' to manage the connection life-cycle
    async with vcaio.ApiClient(configuration) as api_client:
        endpoints_client = vcaio.EndpointsApi(api_client)
        index = "initial-access"

        # 'await' the coroutine to get the actual response data
        api_response = await endpoints_client.backup_index_get(index)

        if not api_response.data:
            print("No backup URL found.")
            return

        download_url = api_response.data[0].url
        file_path = f"{index}.zip"

        print(f"Downloading {index} via requests (offloaded to thread)...")

        # Use asyncio.to_thread to run the blocking requests call safely
        # 'await' the coroutine to get the actual response data
        await asyncio.to_thread(download_sync, download_url, file_path)

        print(f"Successfully saved to {file_path}")


if __name__ == "__main__":
    asyncio.run(main())
