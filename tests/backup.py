import urllib.request
import vulncheck_sdk
import os

DEFAULT_HOST = "https://api.vulncheck.com"
DEFAULT_API = DEFAULT_HOST + "/v3"
TOKEN = os.environ["VULNCHECK_API_TOKEN"]

configuration = vulncheck_sdk.Configuration(host=DEFAULT_API, ignore_operation_servers=True)
configuration.api_key["Bearer"] = TOKEN

with vulncheck_sdk.ApiClient(configuration) as api_client:
    endpoints_client = vulncheck_sdk.EndpointsApi(api_client)

    index = "initial-access"

    api_response = endpoints_client.backup_index_get(index)

    file_path = f"{index}.zip"
    with urllib.request.urlopen(api_response.data[0].url) as response:
        with open(file_path, "wb") as file:
            file.write(response.read())
