<p align="center">
    <img src="/logo-sdk.png" align="center" alt="VulnCheck Logo" width="150" />
</p>

# The VulnCheck SDK

Bring the VulnCheck API to your Python applications.

## Installation

```sh
# Directly from github
pip install git+https://github.com/vulncheck-oss/sdk-python.git

# From PyPi
pip install vulncheck-sdk

```

> [!IMPORTANT]
> Windows users may need to enable [Long Path Support](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry#enable-long-paths-in-windows-10-version-1607-and-later)

## Quickstart

### Connecting to the API

```python
import vulncheck_sdk

DEFAULT_HOST = "https://api.vulncheck.com"
DEFAULT_API = DEFAULT_HOST + "/v3"
TOKEN = os.environ["VULNCHECK_API_TOKEN"]

configuration = vulncheck_sdk.Configuration(host=DEFAULT_API)
configuration.api_key["Bearer"] = TOKEN

with vulncheck_sdk.ApiClient(configuration) as api_client:
    # For purl, cpe, backup, tags, pdns, etc.
    endpoints_client = vulncheck_sdk.EndpointsApi(api_client)
    # For querying an individual index
    indices_client = vulncheck_sdk.IndicesApi(api_client)
```

> [!NOTE]
> Find more detail in the full [OpenAPI docs](./vulncheck_sdk_README.md)

### PURL

Get the CVE's for a given PURL

```python
import vulncheck_sdk
from vulncheck_sdk.models.v3controllers_purl_response_data import (
    V3controllersPurlResponseData,
)

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
```

### CPE

Get all CPE's related to a CVE

```python
import vulncheck_sdk

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
```

### Backup

Download the backup for an index

```python
import requests
import vulncheck_sdk

DEFAULT_HOST = "https://api.vulncheck.com"
DEFAULT_API = DEFAULT_HOST + "/v3"
TOKEN = os.environ["VULNCHECK_API_TOKEN"]

configuration = vulncheck_sdk.Configuration(host=DEFAULT_API)
configuration.api_key["Bearer"] = TOKEN

with vulncheck_sdk.ApiClient(configuration) as api_client:
    endpoints_client = vulncheck_sdk.EndpointsApi(api_client)

    index = "initial-access"

    api_response = endpoints_client.backup_index_get(index)

    backup_url = requests.get(api_response.data[0].url)

    file_path = f"{index}.zip"
    with open(file_path, "wb") as file:
      file.write(backup_url.content)
```

### Indices

Get all available indices

```python
import vulncheck_sdk

DEFAULT_HOST = "https://api.vulncheck.com"
DEFAULT_API = DEFAULT_HOST + "/v3"
TOKEN = os.environ["VULNCHECK_API_TOKEN"]

configuration = vulncheck_sdk.Configuration(host=DEFAULT_API)
configuration.api_key["Bearer"] = TOKEN

with vulncheck_sdk.ApiClient(configuration) as api_client:
    endpoints_client = vulncheck_sdk.EndpointsApi(api_client)

    api_response = endpoints_client.index_get()

    for index in api_response.data:
        print(index.name)
```

### Index

Query VulnCheck-NVD2 for `CVE-2019-19781`

```python
import vulncheck_sdk

DEFAULT_HOST = "https://api.vulncheck.com"
DEFAULT_API = DEFAULT_HOST + "/v3"
TOKEN = os.environ["VULNCHECK_API_TOKEN"]

configuration = vulncheck_sdk.Configuration(host=DEFAULT_API)
configuration.api_key["Bearer"] = TOKEN

with vulncheck_sdk.ApiClient(configuration) as api_client:
    indices_client = vulncheck_sdk.IndicesApi(api_client)

    query_params = vulncheck_sdk.ParamsIdxReqParams(cve="CVE-2019-19781")
    api_response = indices_client.index_vulncheck_nvd2_get(query_params)

    print(api_response.data)
```

### Pagination

With a limit of 10 findings, get the first 5 pages of results from `ipintel-3d`

```python
import vulncheck_sdk
from vulncheck_sdk.models.paginate_pagination import PaginatePagination

DEFAULT_HOST = "https://api.vulncheck.com"
DEFAULT_API = DEFAULT_HOST + "/v3"
TOKEN = os.environ["VULNCHECK_API_TOKEN"]

configuration = vulncheck_sdk.Configuration(host=DEFAULT_API)
configuration.api_key["Bearer"] = TOKEN

with vulncheck_sdk.ApiClient(configuration) as api_client:
    indices_client = vulncheck_sdk.IndicesApi(api_client)
    query_params = vulncheck_sdk.ParamsIdxReqParams()

    limit = 10
    page = 1

    while page <= 5:
        api_response = indices_client.index_ipintel3d_get(
            query_params, limit=limit, page=page
        )
        print(f"Page {page}:")
        print(api_response.data)

        meta: PaginatePagination = api_response.meta
        if meta.page >= meta.total_pages:
            break
        page += 1
```

## License

Apache License 2.0. Please see License File for more information.
