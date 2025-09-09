<p align="center">
    <img src="https://raw.githubusercontent.com/vulncheck-oss/sdk-python/refs/heads/main/logo-sdk.png" align="center" alt="VulnCheck Logo" width="150" />
</p>

# The VulnCheck SDK For Python

Bring the VulnCheck API to your Python applications.

[![PyPI - Version](https://badge.fury.io/py/vulncheck-sdk.svg)](https://badge.fury.io/py/vulncheck-sdk)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626.svg?style=flat&logo=Jupyter)](https://jupyter.org/)

<!--toc:start-->
- [The VulnCheck SDK For Python](#the-vulncheck-sdk-for-python)
  - [Installation](#installation)
  - [Resources](#resources)
  - [Quickstart](#quickstart)
  - [Examples](#examples)
    - [PURL](#purl)
    - [CPE](#cpe)
    - [Backup](#backup)
    - [Indices](#indices)
    - [Index](#index)
    - [Pagination](#pagination)
  - [Contributing](#contributing)
  - [Security](#security)
  - [Sponsorship](#sponsorship)
  - [License](#license)
<!--toc:end-->

## Installation

```sh
# From PyPi
pip install vulncheck-sdk
```

> [!IMPORTANT]
> Windows users may need to enable [Long Path Support](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=registry#enable-long-paths-in-windows-10-version-1607-and-later)

## Resources

- [OpenAPI Documentation](./vulncheck_sdk_README.md)
- [VulnCheck API Docs](https://docs.vulncheck.com/api)
- [VulnCheck Python SDK Docs](https://docs.vulncheck.com/tools/python-sdk/introduction)

## Quickstart

```python
import vulncheck_sdk

# First let's setup a few variables to help us
DEFAULT_HOST = "https://api.vulncheck.com"
DEFAULT_API = DEFAULT_HOST + "/v3"
TOKEN = os.environ["VULNCHECK_API_TOKEN"] # Remember to store your token securely!

# Now let's create a configuration object
configuration = vulncheck_sdk.Configuration(host=DEFAULT_API)
configuration.api_key["Bearer"] = TOKEN

# Pass that config object to our API client and now...
with vulncheck_sdk.ApiClient(configuration) as api_client:
    # We can use two classes to explore the VulnCheck API: EndpointsApi & IndicesApi

    ### EndpointsApi has methods to query every endpoint except `/v3/index`
    # See the full list of endpoints here: https://docs.vulncheck.com/api
    endpoints_client = vulncheck_sdk.EndpointsApi(api_client)

    # PURL
    api_response = endpoints_client.purl_get("pkg:hex/coherence@0.1.2")
    data: V3controllersPurlResponseData = api_response.data
    print(data.cves)

    # CPE
    cpe = "cpe:/a:microsoft:internet_explorer:8.0.6001:beta"
    api_response = endpoints_client.cpe_get(cpe)
    for cve in api_response.data:
        print(cve)

    # Download a Backup
    api_response = endpoints_client.backup_index_get("initial-access")
    backup_url = requests.get(api_response.data[0].url)
    file_path = f"{index}.zip"
    with open(file_path, "wb") as file:
      file.write(backup_url.content)

    ### IndicesApi has methods for each index
    indices_client = vulncheck_sdk.IndicesApi(api_client)

    # Add query parameters to filter what you need
    api_response = indices_client.index_vulncheck_nvd2_get(cve="CVE-2019-19781")

    print(api_response.data)
```

## Examples

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

    api_response = indices_client.index_vulncheck_nvd2_get(cve="CVE-2019-19781")

    print(api_response.data)
```

### Pagination

Paginate over results for a query to VulnCheck-KEV using `cursor`

```python
import vulncheck_sdk

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
```

## Contributing

Please see [CONTRIBUTING](./.github/CONTRIBUTING.md) for details.

## Security

If you discover any security related issues, please create an [issue](https://github.com/vulncheck-oss/sdk-python/issues/new?template=1_BUG-FORM.yaml).

## Sponsorship

Development of this project is sponsored by [VulnCheck](https://vulncheck.com/) learn more about us!

## License

Apache License 2.0. Please see [License File](./LICENSE) for more information.
