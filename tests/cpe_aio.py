import asyncio
import os
import vulncheck_sdk.aio as vcaio

# Configuration
DEFAULT_HOST = "https://api.vulncheck.com"
DEFAULT_API = DEFAULT_HOST + "/v3"
TOKEN = os.environ.get("VULNCHECK_API_TOKEN")

configuration = vcaio.Configuration(host=DEFAULT_API)
configuration.api_key["Bearer"] = TOKEN


async def get_cpe_vulnerabilities():
    # 'async with' to manage the connection life-cycle
    async with vcaio.ApiClient(configuration) as api_client:
        endpoints_client = vcaio.EndpointsApi(api_client)

        cpe = "cpe:/a:microsoft:internet_explorer:8.0.6001:beta"

        # 'await' the coroutine to get the actual response data
        api_response = await endpoints_client.cpe_get(cpe)

        # Iterate through the results
        if api_response.data:
            for cve in api_response.data:
                print(cve)
        else:
            print(f"No vulnerabilities found for CPE: {cpe}")


if __name__ == "__main__":
    # Run the main async entry point
    asyncio.run(get_cpe_vulnerabilities())
