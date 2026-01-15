import asyncio
import os
import vulncheck_sdk.aio as vcaio

# Configuration
DEFAULT_HOST = "https://api.vulncheck.com"
DEFAULT_API = DEFAULT_HOST + "/v3"
TOKEN = os.environ.get("VULNCHECK_API_TOKEN")

configuration = vcaio.Configuration(host=DEFAULT_API)
configuration.api_key["Bearer"] = TOKEN


async def get_cve_details():
    # Use 'async with' for the ApiClient
    async with vcaio.ApiClient(configuration) as api_client:
        indices_client = vcaio.IndicesApi(api_client)

        # 'await' the API call
        api_response = await indices_client.index_vulncheck_nvd2_get(
            cve="CVE-2019-19781"
        )

        # Access and print the data
        if api_response.data:
            print(api_response.data)
        else:
            print("No data found for the specified CVE.")


if __name__ == "__main__":
    # Start the async event loop
    asyncio.run(get_cve_details())
