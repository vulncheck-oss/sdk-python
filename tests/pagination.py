import vulncheck_sdk
import os

DEFAULT_HOST = "https://api.vulncheck.com"
DEFAULT_API = DEFAULT_HOST + "/v3"
TOKEN = os.environ["VULNCHECK_API_TOKEN"]

configuration = vulncheck_sdk.Configuration(host=DEFAULT_API)
configuration.api_key["Bearer"] = TOKEN

with vulncheck_sdk.ApiClient(configuration) as api_client:
    indices_client = vulncheck_sdk.IndicesApi(api_client)
    api_response = indices_client.index_vulncheck_kev_get(
        start_cursor="true",
        # `limit` increases the size of each page, making it faster
        # to download large datasets
        limit = 300
    )

    print(api_response.data)

    while api_response.meta.next_cursor is not None:
        api_response = indices_client.index_vulncheck_kev_get(
            cursor=api_response.meta.next_cursor
        )
        print(api_response.data)
