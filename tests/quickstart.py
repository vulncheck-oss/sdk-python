import vulncheck_sdk
import os
import requests

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
    data= V3controllersPurlResponseData = api_response.data
    print(data.cves)

    # CPE
    cpe = "cpe:/a:microsoft:internet_explorer:8.0.6001:beta"
    api_response = endpoints_client.cpe_get(cpe)
    for cve in api_response.data:
        print(cve)

    # Download a Backup
    index = "initial-access"
    api_response = endpoints_client.backup_index_get(index)
    backup_url = requests.get(api_response.data[0].url)
    
    file_path = f"{index}.zip"
    with open(file_path, "wb") as file:
      file.write(backup_url.content)

    ### IndicesApi has methods for each index
    indices_client = vulncheck_sdk.IndicesApi(api_client)

    # Add query parameters to filter what you need
    api_response = indices_client.index_vulncheck_nvd2_get(cve="CVE-2019-19781")

    print(api_response.data)
