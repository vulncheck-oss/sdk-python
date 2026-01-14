import vulncheck_sdk
from vulncheck_sdk.models.v3controllers_purl_response_data import (
    V3controllersPurlResponseData,
)
import os

DEFAULT_HOST = "https://api.vulncheck.com"
DEFAULT_API = DEFAULT_HOST + "/v3"
TOKEN = os.environ["VULNCHECK_API_TOKEN"]

configuration = vulncheck_sdk.Configuration(host=DEFAULT_API)
configuration.api_key["Bearer"] = TOKEN

with vulncheck_sdk.ApiClient(configuration) as api_client:
    endpoints_client = vulncheck_sdk.EndpointsApi(api_client)

    purl = "pkg:hex/coherence@0.1.2"

    api_response = endpoints_client.purl_get(purl)
    data: V3controllersPurlResponseData = api_response.data

    print(data.cves)
