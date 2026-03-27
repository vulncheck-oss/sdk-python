# vulncheck_sdk.BackupApi

All URIs are relative to *https://api.vulncheck.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backup_get**](BackupApi.md#backup_get) | **GET** /backup | List available backups
[**backup_index_get**](BackupApi.md#backup_index_get) | **GET** /backup/{index} | Get backup by feed name


# **backup_get**
> BackupListBackupsResponse backup_get()

List available backups

Returns the list of advisory feeds for which a backup can be requested

### Example

* Api Key Authentication (Bearer):

```python
import vulncheck_sdk
from vulncheck_sdk.models.backup_list_backups_response import BackupListBackupsResponse
from vulncheck_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.vulncheck.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = vulncheck_sdk.Configuration(
    host = "https://api.vulncheck.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with vulncheck_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vulncheck_sdk.BackupApi(api_client)

    try:
        # List available backups
        api_response = api_instance.backup_get()
        print("The response of BackupApi->backup_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->backup_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BackupListBackupsResponse**](BackupListBackupsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backup_index_get**
> BackupBackupResponse backup_index_get(index)

Get backup by feed name

Validates the feed, generates a fresh backup zip if the source parquet is newer, and returns a pre-signed download URL

### Example

* Api Key Authentication (Bearer):

```python
import vulncheck_sdk
from vulncheck_sdk.models.backup_backup_response import BackupBackupResponse
from vulncheck_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.vulncheck.com/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = vulncheck_sdk.Configuration(
    host = "https://api.vulncheck.com/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with vulncheck_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = vulncheck_sdk.BackupApi(api_client)
    index = 'index_example' # str | Feed name (e.g. 'vulncheck')

    try:
        # Get backup by feed name
        api_response = api_instance.backup_index_get(index)
        print("The response of BackupApi->backup_index_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BackupApi->backup_index_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| Feed name (e.g. &#39;vulncheck&#39;) | 

### Return type

[**BackupBackupResponse**](BackupBackupResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

