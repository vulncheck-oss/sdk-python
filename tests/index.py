import vulncheck_sdk
import os

TOKEN = os.environ["VULNCHECK_API_TOKEN"]

configuration = vulncheck_sdk.Configuration()
configuration.api_key["Bearer"] = TOKEN

with vulncheck_sdk.ApiClient(configuration) as api_client:
    indices_client = vulncheck_sdk.IndicesApi(api_client)

    api_response = indices_client.index_vulncheck_nvd2_get(cve="CVE-2019-19781")

    print(api_response.data)
