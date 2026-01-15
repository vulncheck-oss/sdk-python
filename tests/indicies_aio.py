import asyncio
import os
import vulncheck_sdk.aio as vcaio

# Configuration
DEFAULT_HOST = "https://api.vulncheck.com"
DEFAULT_API = DEFAULT_HOST + "/v3"
TOKEN = os.environ.get("VULNCHECK_API_TOKEN")

configuration = vcaio.Configuration(host=DEFAULT_API)
configuration.api_key["Bearer"] = TOKEN


async def list_indices():
    # Use 'async with' to manage the connection life-cycle
    async with vcaio.ApiClient(configuration) as api_client:
        endpoints_client = vcaio.EndpointsApi(api_client)

        # 'await' the coroutine to get the actual response
        api_response = await endpoints_client.index_get()

        # Iterate through the results
        if api_response.data:
            print(f"{'Index Name':<30} | {'Description'}")
            print("-" * 50)
            for index in api_response.data:
                print(f"{index.name:<30}")
        else:
            print("No indices found.")


if __name__ == "__main__":
    # 4. Entry point to run the asynchronous event loop
    asyncio.run(list_indices())
