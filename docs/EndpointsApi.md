# vulncheck_sdk.EndpointsApi

All URIs are relative to */v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backup_get**](EndpointsApi.md#backup_get) | **GET** /backup | Return a list of indexes with backup and endpoint links
[**backup_index_get**](EndpointsApi.md#backup_index_get) | **GET** /backup/{index} | Retrieve a list of backups by index
[**cpe_get**](EndpointsApi.md#cpe_get) | **GET** /cpe | Return CVE &#39;s associated with a specific NIST CPE
[**entitlements_get**](EndpointsApi.md#entitlements_get) | **GET** /entitlements | Retrieve user entitlements
[**index_get**](EndpointsApi.md#index_get) | **GET** /index | Return a list of available indexes with endpoint links
[**openapi_get**](EndpointsApi.md#openapi_get) | **GET** /openapi | Return OpenAPI specification
[**pdns_vulncheck_c2_get**](EndpointsApi.md#pdns_vulncheck_c2_get) | **GET** /pdns/vulncheck-c2 | Retrieve a list of C2 Hostnames
[**purl_get**](EndpointsApi.md#purl_get) | **GET** /purl | Request vulnerabilities related to a PURL
[**purls_post**](EndpointsApi.md#purls_post) | **POST** /purls | Request vulnerabilities related to a list of PURLs
[**rules_initial_access_type_get**](EndpointsApi.md#rules_initial_access_type_get) | **GET** /rules/initial-access/{type} | Retrieve set of initial-access detection rules
[**tags_vulncheck_c2_get**](EndpointsApi.md#tags_vulncheck_c2_get) | **GET** /tags/vulncheck-c2 | Retrieve a list of C2 IP addresses


# **backup_get**
> RenderResponseArrayParamsIndexBackupList backup_get()

Return a list of indexes with backup and endpoint links

Return a list of indexes with backup and endpoint links that the user has access to

### Example

* Api Key Authentication (Bearer):

```python
import vulncheck_sdk
from vulncheck_sdk.models.render_response_array_params_index_backup_list import RenderResponseArrayParamsIndexBackupList
from vulncheck_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v3
# See configuration.py for a list of all supported configuration parameters.
configuration = vulncheck_sdk.Configuration(
    host = "/v3"
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
    api_instance = vulncheck_sdk.EndpointsApi(api_client)

    try:
        # Return a list of indexes with backup and endpoint links
        api_response = api_instance.backup_get()
        print("The response of EndpointsApi->backup_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->backup_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RenderResponseArrayParamsIndexBackupList**](RenderResponseArrayParamsIndexBackupList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **backup_index_get**
> RenderResponseWithMetadataV3controllersBackupResponseDataV3controllersBackupResponseMetadata backup_index_get(index)

Retrieve a list of backups by index

Retrieve a list of VulnCheck backups by index

### Example

* Api Key Authentication (Bearer):

```python
import vulncheck_sdk
from vulncheck_sdk.models.render_response_with_metadata_v3controllers_backup_response_data_v3controllers_backup_response_metadata import RenderResponseWithMetadataV3controllersBackupResponseDataV3controllersBackupResponseMetadata
from vulncheck_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v3
# See configuration.py for a list of all supported configuration parameters.
configuration = vulncheck_sdk.Configuration(
    host = "/v3"
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
    api_instance = vulncheck_sdk.EndpointsApi(api_client)
    index = 'index_example' # str | Name of an exploit, vulnerability, or advisory index

    try:
        # Retrieve a list of backups by index
        api_response = api_instance.backup_index_get(index)
        print("The response of EndpointsApi->backup_index_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->backup_index_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| Name of an exploit, vulnerability, or advisory index | 

### Return type

[**RenderResponseWithMetadataV3controllersBackupResponseDataV3controllersBackupResponseMetadata**](RenderResponseWithMetadataV3controllersBackupResponseDataV3controllersBackupResponseMetadata.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cpe_get**
> RenderResponseWithMetadataArrayStringV3controllersResponseMetadata cpe_get(cpe, is_vulnerable=is_vulnerable)

Return CVE 's associated with a specific NIST CPE

Based on the specified CPE (Common Platform Enumeration) URI string, this endpoint will return a list of vulnerabilities that are related to the package. We support v2.2 and v2.3

### Example

* Api Key Authentication (Bearer):

```python
import vulncheck_sdk
from vulncheck_sdk.models.render_response_with_metadata_array_string_v3controllers_response_metadata import RenderResponseWithMetadataArrayStringV3controllersResponseMetadata
from vulncheck_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v3
# See configuration.py for a list of all supported configuration parameters.
configuration = vulncheck_sdk.Configuration(
    host = "/v3"
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
    api_instance = vulncheck_sdk.EndpointsApi(api_client)
    cpe = 'cpe_example' # str | CPE designation to lookup
    is_vulnerable = 'is_vulnerable_example' # str | Filter by vulnerability status (true/false). Defaults to false if not provided. (optional)

    try:
        # Return CVE 's associated with a specific NIST CPE
        api_response = api_instance.cpe_get(cpe, is_vulnerable=is_vulnerable)
        print("The response of EndpointsApi->cpe_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->cpe_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpe** | **str**| CPE designation to lookup | 
 **is_vulnerable** | **str**| Filter by vulnerability status (true/false). Defaults to false if not provided. | [optional] 

### Return type

[**RenderResponseWithMetadataArrayStringV3controllersResponseMetadata**](RenderResponseWithMetadataArrayStringV3controllersResponseMetadata.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **entitlements_get**
> ModelsEntitlements entitlements_get()

Retrieve user entitlements

Retrieve entitlements for the current user

### Example

* Api Key Authentication (Bearer):

```python
import vulncheck_sdk
from vulncheck_sdk.models.models_entitlements import ModelsEntitlements
from vulncheck_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v3
# See configuration.py for a list of all supported configuration parameters.
configuration = vulncheck_sdk.Configuration(
    host = "/v3"
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
    api_instance = vulncheck_sdk.EndpointsApi(api_client)

    try:
        # Retrieve user entitlements
        api_response = api_instance.entitlements_get()
        print("The response of EndpointsApi->entitlements_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->entitlements_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ModelsEntitlements**](ModelsEntitlements.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_get**
> RenderResponseArrayParamsIndexList index_get()

Return a list of available indexes with endpoint links

Return a list of available indexes with endpoint links that the user has access to

### Example

* Api Key Authentication (Bearer):

```python
import vulncheck_sdk
from vulncheck_sdk.models.render_response_array_params_index_list import RenderResponseArrayParamsIndexList
from vulncheck_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v3
# See configuration.py for a list of all supported configuration parameters.
configuration = vulncheck_sdk.Configuration(
    host = "/v3"
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
    api_instance = vulncheck_sdk.EndpointsApi(api_client)

    try:
        # Return a list of available indexes with endpoint links
        api_response = api_instance.index_get()
        print("The response of EndpointsApi->index_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->index_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RenderResponseArrayParamsIndexList**](RenderResponseArrayParamsIndexList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **openapi_get**
> Dict[str, object] openapi_get()

Return OpenAPI specification

Return the VulnCheck API (v3) OpenAPI specification

### Example

* Api Key Authentication (Bearer):

```python
import vulncheck_sdk
from vulncheck_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v3
# See configuration.py for a list of all supported configuration parameters.
configuration = vulncheck_sdk.Configuration(
    host = "/v3"
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
    api_instance = vulncheck_sdk.EndpointsApi(api_client)

    try:
        # Return OpenAPI specification
        api_response = api_instance.openapi_get()
        print("The response of EndpointsApi->openapi_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->openapi_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pdns_vulncheck_c2_get**
> str pdns_vulncheck_c2_get(format=format)

Retrieve a list of C2 Hostnames

Retrieve a list of hostnames, identified as running Command & Control infrastructure.

### Example

* Api Key Authentication (Bearer):

```python
import vulncheck_sdk
from vulncheck_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v3
# See configuration.py for a list of all supported configuration parameters.
configuration = vulncheck_sdk.Configuration(
    host = "/v3"
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
    api_instance = vulncheck_sdk.EndpointsApi(api_client)
    format = 'format_example' # str | Format of the Hostnames in the response (Defaults To: text) (optional)

    try:
        # Retrieve a list of C2 Hostnames
        api_response = api_instance.pdns_vulncheck_c2_get(format=format)
        print("The response of EndpointsApi->pdns_vulncheck_c2_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->pdns_vulncheck_c2_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Format of the Hostnames in the response (Defaults To: text) | [optional] 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purl_get**
> RenderResponseWithMetadataV3controllersPurlResponseDataV3controllersPurlResponseMetadata purl_get(purl)

Request vulnerabilities related to a PURL

Based on the specified PURL, this endpoint will return a list of vulnerabilities that are related to the package. We currently support hex, golang, hackage, npm, and pypi

### Example

* Api Key Authentication (Bearer):

```python
import vulncheck_sdk
from vulncheck_sdk.models.render_response_with_metadata_v3controllers_purl_response_data_v3controllers_purl_response_metadata import RenderResponseWithMetadataV3controllersPurlResponseDataV3controllersPurlResponseMetadata
from vulncheck_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v3
# See configuration.py for a list of all supported configuration parameters.
configuration = vulncheck_sdk.Configuration(
    host = "/v3"
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
    api_instance = vulncheck_sdk.EndpointsApi(api_client)
    purl = 'purl_example' # str | URL string used to identify and locate a software package

    try:
        # Request vulnerabilities related to a PURL
        api_response = api_instance.purl_get(purl)
        print("The response of EndpointsApi->purl_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->purl_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purl** | **str**| URL string used to identify and locate a software package | 

### Return type

[**RenderResponseWithMetadataV3controllersPurlResponseDataV3controllersPurlResponseMetadata**](RenderResponseWithMetadataV3controllersPurlResponseDataV3controllersPurlResponseMetadata.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purls_post**
> RenderResponseWithMetadataV3controllersPurlsResponseDataV3controllersPurlsResponseMetadata purls_post(purls)

Request vulnerabilities related to a list of PURLs

Accepts a JSON array of PURLs in the request body and returns a list of vulnerabilities

### Example

* Api Key Authentication (Bearer):

```python
import vulncheck_sdk
from vulncheck_sdk.models.render_response_with_metadata_v3controllers_purls_response_data_v3controllers_purls_response_metadata import RenderResponseWithMetadataV3controllersPurlsResponseDataV3controllersPurlsResponseMetadata
from vulncheck_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v3
# See configuration.py for a list of all supported configuration parameters.
configuration = vulncheck_sdk.Configuration(
    host = "/v3"
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
    api_instance = vulncheck_sdk.EndpointsApi(api_client)
    purls = ['purls_example'] # List[str] | PURL strings used to identify and locate software packages

    try:
        # Request vulnerabilities related to a list of PURLs
        api_response = api_instance.purls_post(purls)
        print("The response of EndpointsApi->purls_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->purls_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **purls** | [**List[str]**](str.md)| PURL strings used to identify and locate software packages | 

### Return type

[**RenderResponseWithMetadataV3controllersPurlsResponseDataV3controllersPurlsResponseMetadata**](RenderResponseWithMetadataV3controllersPurlsResponseDataV3controllersPurlsResponseMetadata.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rules_initial_access_type_get**
> str rules_initial_access_type_get(type)

Retrieve set of initial-access detection rules

Retrieve set of initial-access detection rules by type

### Example

* Api Key Authentication (Bearer):

```python
import vulncheck_sdk
from vulncheck_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v3
# See configuration.py for a list of all supported configuration parameters.
configuration = vulncheck_sdk.Configuration(
    host = "/v3"
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
    api_instance = vulncheck_sdk.EndpointsApi(api_client)
    type = 'type_example' # str | Type of ruleset to retrieve

    try:
        # Retrieve set of initial-access detection rules
        api_response = api_instance.rules_initial_access_type_get(type)
        print("The response of EndpointsApi->rules_initial_access_type_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->rules_initial_access_type_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Type of ruleset to retrieve | 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_vulncheck_c2_get**
> str tags_vulncheck_c2_get(format=format)

Retrieve a list of C2 IP addresses

Retrieve a list of IP addresses, identified as running Command & Control infrastructure

### Example

* Api Key Authentication (Bearer):

```python
import vulncheck_sdk
from vulncheck_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /v3
# See configuration.py for a list of all supported configuration parameters.
configuration = vulncheck_sdk.Configuration(
    host = "/v3"
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
    api_instance = vulncheck_sdk.EndpointsApi(api_client)
    format = 'format_example' # str | Format of the IP Addresses in the response (Defaults To: text) (optional)

    try:
        # Retrieve a list of C2 IP addresses
        api_response = api_instance.tags_vulncheck_c2_get(format=format)
        print("The response of EndpointsApi->tags_vulncheck_c2_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->tags_vulncheck_c2_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| Format of the IP Addresses in the response (Defaults To: text) | [optional] 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

