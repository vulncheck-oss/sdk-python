import json
import urllib.request
import vulncheck_sdk
import os

TOKEN = os.environ["VULNCHECK_API_TOKEN"]

configuration = vulncheck_sdk.Configuration()
configuration.api_key["Bearer"] = TOKEN

with vulncheck_sdk.ApiClient(configuration) as api_client:
    endpoints_client = vulncheck_sdk.EndpointsApi(api_client)

    index = "initial-access"

    raw = endpoints_client.backup_index_get_without_preload_content(index)
    response_data = json.loads(raw.read())
    download_url = response_data["data"][0]["url"]

    file_path = f"{index}.zip"
    with urllib.request.urlopen(download_url) as response:
        with open(file_path, "wb") as file:
            file.write(response.read())
