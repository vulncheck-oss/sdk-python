import asyncio
import os
import vulncheck_sdk
from vulncheck_sdk.aio.models.v3controllers_purl_response_data import (
    V3controllersPurlResponseData,
)

# Configuration
DEFAULT_HOST = "https://api.vulncheck.com"
DEFAULT_API = DEFAULT_HOST + "/v3"
TOKEN = os.environ.get("VULNCHECK_API_TOKEN")

configuration = vulncheck_sdk.aio.Configuration(host=DEFAULT_API)
configuration.api_key["Bearer"] = TOKEN

async def get_data(client, purl: str):
    # Await the client call directly
    api_response = await client.purl_get(purl)
    # Access the data attribute from the response object
    return api_response.data

async def main():
    async with vulncheck_sdk.aio.ApiClient(configuration) as api_client:
        endpoints_client = vulncheck_sdk.aio.EndpointsApi(api_client)

        purl = "pkg:hex/coherence@0.1.2"
        
        # 'await' the async function call
        data: V3controllersPurlResponseData = await get_data(endpoints_client, purl)

        if data and data.cves:
            print(f"Found {len(data.cves)} CVEs:")
            for cve in data.cves:
                print(f"- {cve}")
        else:
            print("No CVEs found or data is empty.")

if __name__ == "__main__":
    asyncio.run(main())