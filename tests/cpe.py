import vulncheck_sdk
import os

DEFAULT_HOST = "https://api.vulncheck.com"
DEFAULT_API = DEFAULT_HOST + "/v3"
TOKEN = os.environ["VULNCHECK_API_TOKEN"]

configuration = vulncheck_sdk.Configuration(host=DEFAULT_API)
configuration.api_key["Bearer"] = TOKEN

with vulncheck_sdk.ApiClient(configuration) as api_client:
    endpoints_client = vulncheck_sdk.EndpointsApi(api_client)

    cpe = "cpe:/a:microsoft:internet_explorer:8.0.6001:beta"

    api_response = endpoints_client.cpe_get(cpe)

    for cve in api_response.data:
        print(cve)
