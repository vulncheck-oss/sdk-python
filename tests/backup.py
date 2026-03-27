import json
import urllib.request
import vulncheck_sdk
import os

TOKEN = os.environ["VULNCHECK_API_TOKEN"]

configuration = vulncheck_sdk.Configuration()
configuration.api_key["Bearer"] = TOKEN
configuration.ignore_operation_servers = True

with vulncheck_sdk.ApiClient(configuration) as api_client:
    backup_client = vulncheck_sdk.BackupApi(api_client)

    index = "initial-access"

    raw = backup_client.backup_index_get_without_preload_content(index)
    response_data = json.loads(raw.read())
    download_url = response_data["data"][0]["url"]

    file_path = f"{index}.zip"
    with urllib.request.urlopen(download_url) as response:
        with open(file_path, "wb") as file:
            file.write(response.read())
