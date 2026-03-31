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
    - [Advisory](#advisory)
    - [Backup](#backup)
    - [Backup v4](#backup-v4)
    - [CPE](#cpe)
    - [Index](#index)
    - [Indices](#indices)
    - [Pagination](#pagination)
    - [PURL](#purl)
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
import urllib.request
import vulncheck_sdk
import os

# First let's setup a few variables to help us
TOKEN = os.environ["VULNCHECK_API_TOKEN"]  # Remember to store your token securely!

# Now let's create a configuration object
configuration = vulncheck_sdk.Configuration()
configuration.api_key["Bearer"] = TOKEN

# Pass that config object to our API client and now...
with vulncheck_sdk.ApiClient(configuration) as api_client:
    # We can use two classes to explore the VulnCheck API: EndpointsApi & IndicesApi

    ### EndpointsApi has methods to query every endpoint except `/v3/index`
    # See the full list of endpoints here: https://docs.vulncheck.com/api
    endpoints_client = vulncheck_sdk.EndpointsApi(api_client)

    # PURL
    api_response = endpoints_client.purl_get("pkg:hex/coherence@0.1.2")
    data = V3controllersPurlResponseData = api_response.data
    print(data.cves)

    # CPE
    cpe = "cpe:/a:microsoft:internet_explorer:8.0.6001:beta"
    api_response = endpoints_client.cpe_get(cpe)
    for cve in api_response.data:
        print(cve)

    # Download a Backup
    index = "initial-access"
    api_response = endpoints_client.backup_index_get(index)
    file_path = f"{index}.zip"
    with urllib.request.urlopen(api_response.data[0].url) as response:
        with open(file_path, "wb") as file:
            file.write(response.read())

    ### IndicesApi has methods for each index
    indices_client = vulncheck_sdk.IndicesApi(api_client)

    # Add query parameters to filter what you need
    api_response = indices_client.index_vulncheck_nvd2_get(cve="CVE-2019-19781")

    print(api_response.data)
```


<details><summary><b>Click to View Async Implementation</b></summary>

```python
import asyncio
import os
import aiohttp
import vulncheck_sdk.aio as vcaio

# Configuration
TOKEN = os.environ.get("VULNCHECK_API_TOKEN")

configuration = vcaio.Configuration()
configuration.api_key["Bearer"] = TOKEN


async def run_vulnerability_checks():
    # Use 'async with' to manage the ApiClient connection pool
    async with vcaio.ApiClient(configuration) as api_client:
        endpoints_client = vcaio.EndpointsApi(api_client)
        indices_client = vcaio.IndicesApi(api_client)

        # --- PURL Search ---
        # 'await' the coroutine to get results
        purl_response = await endpoints_client.purl_get("pkg:hex/coherence@0.1.2")
        if purl_response.data:
            print(f"PURL CVEs: {purl_response.data.cves}")

        # --- CPE Search ---
        cpe = "cpe:/a:microsoft:internet_explorer:8.0.6001:beta"
        # 'await' the coroutine to get results
        cpe_response = await endpoints_client.cpe_get(cpe)
        print(f"CPE Results for {cpe}:")
        for cve in cpe_response.data:
            print(f" - {cve}")

        # --- Index Query (NVD2) ---
        # 'await' the coroutine to get results
        nvd_response = await indices_client.index_vulncheck_nvd2_get(
            cve="CVE-2019-19781"
        )
        print(f"NVD2 Data: {nvd_response.data}")

        # --- Download Backup (Async) ---
        index_name = "initial-access"
        # 'await' the coroutine to get results
        backup_response = await endpoints_client.backup_index_get(index_name)

        if backup_response.data:
            download_url = backup_response.data[0].url
            file_path = f"{index_name}.zip"

            print(f"Downloading backup from {download_url}...")
            # Use aiohttp (already in your environment) for async download
            async with aiohttp.ClientSession() as session:
                async with session.get(download_url) as resp:
                    if resp.status == 200:
                        # 'await' the coroutine to get results
                        content = await resp.read()
                        with open(file_path, "wb") as f:
                            f.write(content)
                        print(f"Saved backup to {file_path}")


if __name__ == "__main__":
    # Entry point to start the event loop
    asyncio.run(run_vulnerability_checks())
```


</details>

## Examples

### PURL

Get the CVE's for a given PURL

```python
import vulncheck_sdk
from vulncheck_sdk.models.v3controllers_purl_response_data import (
    V3controllersPurlResponseData,
)
import os

TOKEN = os.environ["VULNCHECK_API_TOKEN"]

configuration = vulncheck_sdk.Configuration()
configuration.api_key["Bearer"] = TOKEN

with vulncheck_sdk.ApiClient(configuration) as api_client:
    endpoints_client = vulncheck_sdk.EndpointsApi(api_client)

    purl = "pkg:hex/coherence@0.1.2"

    api_response = endpoints_client.purl_get(purl)
    data: V3controllersPurlResponseData = api_response.data

    print(data.cves)
```


<details><summary><b>Click to View Async Implementation</b></summary>

```python
import asyncio
import os
import vulncheck_sdk.aio as vcaio
from vulncheck_sdk.aio.models.v3controllers_purl_response_data import (
    V3controllersPurlResponseData,
)

# Configuration
TOKEN = os.environ.get("VULNCHECK_API_TOKEN")

configuration = vcaio.Configuration()
configuration.api_key["Bearer"] = TOKEN


async def get_data(client, purl: str):
    # Await the client call directly
    api_response = await client.purl_get(purl)

    # Access the data attribute from the response object
    return api_response.data


async def main():
    async with vcaio.ApiClient(configuration) as api_client:
        endpoints_client = vcaio.EndpointsApi(api_client)

        purl = "pkg:hex/coherence@0.1.2"

        # 'await' the async function call
        data: V3controllersPurlResponseData = await get_data(endpoints_client, purl)

        if data and data.cves:
            print(f"Found {len(data.cves)} CVEs:")
            for cve in data.cves:
                print(f"- {cve}")
        else:
            print("No CVEs found or data is empty.")


if __name__ == "__main__":
    asyncio.run(main())
```


</details>

### CPE

Get all CPE's related to a CVE

```python
import vulncheck_sdk
import os

TOKEN = os.environ["VULNCHECK_API_TOKEN"]

configuration = vulncheck_sdk.Configuration()
configuration.api_key["Bearer"] = TOKEN

with vulncheck_sdk.ApiClient(configuration) as api_client:
    endpoints_client = vulncheck_sdk.EndpointsApi(api_client)

    cpe = "cpe:/a:microsoft:internet_explorer:8.0.6001:beta"

    api_response = endpoints_client.cpe_get(cpe)

    for cve in api_response.data:
        print(cve)
```


<details><summary><b>Click to View Async Implementation</b></summary>

```python
import asyncio
import os
import vulncheck_sdk.aio as vcaio

# Configuration
TOKEN = os.environ.get("VULNCHECK_API_TOKEN")

configuration = vcaio.Configuration()
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
```


</details>

### Backup

Download the backup for an index

```python
import urllib.request
import vulncheck_sdk
import os

TOKEN = os.environ["VULNCHECK_API_TOKEN"]

configuration = vulncheck_sdk.Configuration()
configuration.api_key["Bearer"] = TOKEN

with vulncheck_sdk.ApiClient(configuration) as api_client:
    endpoints_client = vulncheck_sdk.EndpointsApi(api_client)

    index = "initial-access"

    api_response = endpoints_client.backup_index_get(index)

    file_path = f"{index}.zip"
    with urllib.request.urlopen(api_response.data[0].url) as response:
        with open(file_path, "wb") as file:
            file.write(response.read())
```


<details><summary><b>Click to View Async Implementation</b></summary>

```python
import asyncio
import os
import urllib.request
import vulncheck_sdk.aio as vcaio

# Configuration
TOKEN = os.environ.get("VULNCHECK_API_TOKEN")

configuration = vcaio.Configuration()
configuration.api_key["Bearer"] = TOKEN


def download_sync(url, file_path):
    """
    Standard synchronous download using urllib.request.
    This runs in a separate thread to avoid blocking the event loop.
    """
    with urllib.request.urlopen(url) as response:
        with open(file_path, "wb") as file:
            file.write(response.read())


async def main():
    # Use 'async with' to manage the connection life-cycle
    async with vcaio.ApiClient(configuration) as api_client:
        endpoints_client = vcaio.EndpointsApi(api_client)
        index = "initial-access"

        # 'await' the coroutine to get the actual response data
        api_response = await endpoints_client.backup_index_get(index)

        if not api_response.data:
            print("No backup URL found.")
            return

        download_url = api_response.data[0].url
        file_path = f"{index}.zip"

        print(f"Downloading {index} via urllib (offloaded to thread)...")

        # Use asyncio.to_thread to run the blocking call safely
        # 'await' the coroutine to get the actual response data
        await asyncio.to_thread(download_sync, download_url, file_path)

        print(f"Successfully saved to {file_path}")


if __name__ == "__main__":
    asyncio.run(main())
```


</details>

### Advisory

List all advisory feeds and query advisories filtered by feed

```python
import vulncheck_sdk
from vulncheck_sdk.models.search_v4_advisory_return_value import SearchV4AdvisoryReturnValue
from vulncheck_sdk.models.search_v4_list_feed_return_value import SearchV4ListFeedReturnValue
import os

TOKEN = os.environ["VULNCHECK_API_TOKEN"]

configuration = vulncheck_sdk.Configuration()
configuration.api_key["Bearer"] = TOKEN

with vulncheck_sdk.ApiClient(configuration) as api_client:
    advisory_client = vulncheck_sdk.AdvisoryApi(api_client)

    # List all available advisory feeds (/v4/advisory)
    feeds: SearchV4ListFeedReturnValue = advisory_client.v4_list_advisory_feeds()
    print("Available feeds:")
    for feed in feeds.data:
        print(f"name: {feed.name}")

    feed = "wolfi"
    # Query advisories filtered by feed=wolfi (/v4/advisory?feed=wolfi)
    advisories: SearchV4AdvisoryReturnValue = advisory_client.v4_query_advisories(name=feed)
    print(f"{feed.capitalize()} advisories (page 1): {len(advisories.data)} results")
    for advisory in advisories.data:
        print(f"cve: {advisory.cve_metadata.cve_id}")
```


<details><summary><b>Click to View Async Implementation</b></summary>

```python
import asyncio
import os
import vulncheck_sdk.aio as vcaio
from vulncheck_sdk.aio.models.search_v4_advisory_return_value import SearchV4AdvisoryReturnValue
from vulncheck_sdk.aio.models.search_v4_list_feed_return_value import SearchV4ListFeedReturnValue

TOKEN = os.environ.get("VULNCHECK_API_TOKEN")

configuration = vcaio.Configuration()
configuration.api_key["Bearer"] = TOKEN


async def main():
    async with vcaio.ApiClient(configuration) as api_client:
        advisory_client = vcaio.AdvisoryApi(api_client)

        # List all available advisory feeds (/v4/advisory)
        feeds: SearchV4ListFeedReturnValue = await advisory_client.v4_list_advisory_feeds()
        print("Available feeds:")
        for feed in feeds.data:
            print(f"name: {feed.name}")

        feed = "wolfi"
        # Query advisories filtered by feed=wolfi (/v4/advisory?feed=wolfi)
        advisories: SearchV4AdvisoryReturnValue = await advisory_client.v4_query_advisories(name=feed)
        print(f"{feed.capitalize()} advisories (page 1): {len(advisories.data)} results")
        for advisory in advisories.data:
            print(f"cve: {advisory.cve_metadata.cve_id}")


if __name__ == "__main__":
    asyncio.run(main())
```


</details>

### Backup v4

List available v4 backups and download a backup by feed name

```python
import urllib.request
import vulncheck_sdk
from vulncheck_sdk.models.backup_list_backups_response import BackupListBackupsResponse
from vulncheck_sdk.models.backup_feed_item import BackupFeedItem
import os

TOKEN = os.environ["VULNCHECK_API_TOKEN"]

configuration = vulncheck_sdk.Configuration()
configuration.api_key["Bearer"] = TOKEN

with vulncheck_sdk.ApiClient(configuration) as api_client:
    backup_client = vulncheck_sdk.BackupApi(api_client)

    # List available backups (/v4/backup)
    available: BackupListBackupsResponse = backup_client.v4_list_backups()

    for potential_backup in available.data:
        print(f"Found backup: {potential_backup.name}")

    # Get backup for the wolfi feed (/v4/backup/wolfi)
    feed = "wolfi"
    response: BackupListBackupsResponse = backup_client.v4_get_backup_by_name(feed)

    print(f"Downloading {feed} backup")
    file_path = f"{feed}.zip"
    with urllib.request.urlopen(response.url) as r:
        with open(file_path, "wb") as f:
            f.write(r.read())

    print(f"Successfully saved to {file_path}")
```


<details><summary><b>Click to View Async Implementation</b></summary>

```python
import asyncio
import os
import urllib.request
import vulncheck_sdk.aio as vcaio
from vulncheck_sdk.aio.models.backup_list_backups_response import BackupListBackupsResponse
from vulncheck_sdk.aio.models.backup_backup_response import BackupBackupResponse

TOKEN = os.environ.get("VULNCHECK_API_TOKEN")

configuration = vcaio.Configuration()
configuration.api_key["Bearer"] = TOKEN


def download_sync(url, file_path):
    """
    Standard synchronous download using urllib.request.
    This runs in a separate thread to avoid blocking the event loop.
    """
    with urllib.request.urlopen(url) as response:
        with open(file_path, "wb") as file:
            file.write(response.read())


async def main():
    async with vcaio.ApiClient(configuration) as api_client:
        backup_client = vcaio.BackupApi(api_client)

        # List available backups (/v4/backup)
        available: BackupListBackupsResponse = await backup_client.v4_list_backups()
        for potential_backup in available.data:
            print(f"Found backup: {potential_backup.name}")

        # Get backup for the wolfi feed (/v4/backup/wolfi)
        feed = "wolfi"
        response: BackupBackupResponse = await backup_client.v4_get_backup_by_name(feed)


        file_path = f"{feed}.zip"
        print(f"Downloading {feed} backup via urllib (offloaded to thread)...")

        await asyncio.to_thread(download_sync, response.url, file_path)

        print(f"Successfully saved to {file_path}")


if __name__ == "__main__":
    asyncio.run(main())
```


</details>

### Indices

Get all available indices

```python
import vulncheck_sdk
import os

TOKEN = os.environ["VULNCHECK_API_TOKEN"]

configuration = vulncheck_sdk.Configuration()
configuration.api_key["Bearer"] = TOKEN

with vulncheck_sdk.ApiClient(configuration) as api_client:
    endpoints_client = vulncheck_sdk.EndpointsApi(api_client)

    api_response = endpoints_client.index_get()

    for index in api_response.data:
        print(index.name)
```


<details><summary><b>Click to View Async Implementation</b></summary>

```python
import asyncio
import os
import vulncheck_sdk.aio as vcaio

# Configuration
TOKEN = os.environ.get("VULNCHECK_API_TOKEN")

configuration = vcaio.Configuration()
configuration.api_key["Bearer"] = TOKEN


async def list_indices():
    # Use 'async with' to manage the connection life-cycle
    async with vcaio.ApiClient(configuration) as api_client:
        endpoints_client = vcaio.EndpointsApi(api_client)

        # 'await' the coroutine to get the actual response
        api_response = await endpoints_client.index_get()

        # Iterate through the results
        if api_response.data:
            print(f"{'Index Name':<30} | {'Description'}")
            print("-" * 50)
            for index in api_response.data:
                print(f"{index.name:<30}")
        else:
            print("No indices found.")


if __name__ == "__main__":
    # 4. Entry point to run the asynchronous event loop
    asyncio.run(list_indices())
```


</details>

### Index

Query VulnCheck-NVD2 for `CVE-2019-19781`

```python
import vulncheck_sdk
import os

TOKEN = os.environ["VULNCHECK_API_TOKEN"]

configuration = vulncheck_sdk.Configuration()
configuration.api_key["Bearer"] = TOKEN

with vulncheck_sdk.ApiClient(configuration) as api_client:
    indices_client = vulncheck_sdk.IndicesApi(api_client)

    api_response = indices_client.index_vulncheck_nvd2_get(cve="CVE-2019-19781")

    print(api_response.data)
```


<details><summary><b>Click to View Async Implementation</b></summary>

```python
import asyncio
import os
import vulncheck_sdk.aio as vcaio

# Configuration
TOKEN = os.environ.get("VULNCHECK_API_TOKEN")

configuration = vcaio.Configuration()
configuration.api_key["Bearer"] = TOKEN


async def get_cve_details():
    # Use 'async with' for the ApiClient
    async with vcaio.ApiClient(configuration) as api_client:
        indices_client = vcaio.IndicesApi(api_client)

        # 'await' the API call
        api_response = await indices_client.index_vulncheck_nvd2_get(
            cve="CVE-2019-19781"
        )

        # Access and print the data
        if api_response.data:
            print(api_response.data)
        else:
            print("No data found for the specified CVE.")


if __name__ == "__main__":
    # Start the async event loop
    asyncio.run(get_cve_details())
```


</details>

### Pagination

Paginate over results for a query to VulnCheck-KEV using `cursor`

```python
import vulncheck_sdk
import os

TOKEN = os.environ["VULNCHECK_API_TOKEN"]

configuration = vulncheck_sdk.Configuration()
configuration.api_key["Bearer"] = TOKEN

with vulncheck_sdk.ApiClient(configuration) as api_client:
    indices_client = vulncheck_sdk.IndicesApi(api_client)
    api_response = indices_client.index_vulncheck_kev_get(
        start_cursor="true",
        # `limit` increases the size of each page, making it faster
        # to download large datasets
        limit=300,
    )

    print(api_response.data)

    while api_response.meta.next_cursor is not None:
        api_response = indices_client.index_vulncheck_kev_get(
            cursor=api_response.meta.next_cursor
        )
        print(api_response.data)
```


<details><summary><b>Click to View Async Implementation</b></summary>

```python
import asyncio
import os
import vulncheck_sdk.aio as vcaio

# Configuration
TOKEN = os.environ.get("VULNCHECK_API_TOKEN")

configuration = vcaio.Configuration()
configuration.api_key["Bearer"] = TOKEN


async def fetch_kev_data():
    # Use 'async with' to properly manage the lifecycle of the async client
    async with vcaio.ApiClient(configuration) as api_client:
        indices_client = vcaio.IndicesApi(api_client)

        # 'await' the coroutine to get the actual response data
        api_response = await indices_client.index_vulncheck_kev_get(
            start_cursor="true", limit=300
        )

        print(f"Fetched {len(api_response.data)} records...")
        # Process initial data
        # (e.g., save to a list or database)

        # Pagination loop
        while api_response.meta and api_response.meta.next_cursor:
            print(f"Fetching next page: {api_response.meta.next_cursor}")

            # 'await' the coroutine to get the actual response data
            api_response = await indices_client.index_vulncheck_kev_get(
                cursor=api_response.meta.next_cursor, limit=300
            )

            if api_response.data:
                print(f"Fetched {len(api_response.data)} records...")
            else:
                break


if __name__ == "__main__":
    # Entry point to run the async event loop
    asyncio.run(fetch_kev_data())
```


</details>

## Contributing

Please see [CONTRIBUTING](./.github/CONTRIBUTING.md) for details.

## Security

If you discover any security related issues, please create an [issue](https://github.com/vulncheck-oss/sdk-python/issues/new?template=1_BUG-FORM.yaml).

## Sponsorship

Development of this project is sponsored by [VulnCheck](https://vulncheck.com/) learn more about us!

## License

Apache License 2.0. Please see [License File](./LICENSE) for more information.

