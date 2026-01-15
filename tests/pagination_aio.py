import asyncio
import os
import vulncheck_sdk

# Configuration
DEFAULT_HOST = "https://api.vulncheck.com"
DEFAULT_API = DEFAULT_HOST + "/v3"
TOKEN = os.environ.get("VULNCHECK_API_TOKEN")

configuration = vulncheck_sdk.aio.Configuration(host=DEFAULT_API)
configuration.api_key["Bearer"] = TOKEN

async def fetch_kev_data():
    # Use 'async with' to properly manage the lifecycle of the async client
    async with vulncheck_sdk.aio.ApiClient(configuration) as api_client:
        indices_client = vulncheck_sdk.aio.IndicesApi(api_client)
        
        # Initial call - MUST be awaited
        api_response = await indices_client.index_vulncheck_kev_get(
            start_cursor="true",
            limit=300
        )

        print(f"Fetched {len(api_response.data)} records...")
        # Process initial data
        # (e.g., save to a list or database)

        # Pagination loop
        while api_response.meta and api_response.meta.next_cursor:
            print(f"Fetching next page: {api_response.meta.next_cursor}")
            
            # Await the subsequent pages
            api_response = await indices_client.index_vulncheck_kev_get(
                cursor=api_response.meta.next_cursor,
                limit=300
            )
            
            if api_response.data:
                print(f"Fetched {len(api_response.data)} records...")
            else:
                break


if __name__ == "__main__":
    # Entry point to run the async event loop
    asyncio.run(fetch_kev_data())