# vulncheck_sdk.AdvisoryApi

All URIs are relative to *https://api.vulncheck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v4_list_advisory_feeds**](AdvisoryApi.md#v4_list_advisory_feeds) | **GET** /v4/advisory/list | List advisory feeds
[**v4_query_advisories**](AdvisoryApi.md#v4_query_advisories) | **GET** /v4/advisory | Query advisories


# **v4_list_advisory_feeds**
> SearchV4ListFeedReturnValue v4_list_advisory_feeds()

List advisory feeds

Return a list of available advisory feed names

### Example

* Api Key Authentication (Bearer):

```python
import vulncheck_sdk
from vulncheck_sdk.models.search_v4_list_feed_return_value import SearchV4ListFeedReturnValue
from vulncheck_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.vulncheck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = vulncheck_sdk.Configuration(
    host = "https://api.vulncheck.com"
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
    api_instance = vulncheck_sdk.AdvisoryApi(api_client)

    try:
        # List advisory feeds
        api_response = api_instance.v4_list_advisory_feeds()
        print("The response of AdvisoryApi->v4_list_advisory_feeds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdvisoryApi->v4_list_advisory_feeds: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SearchV4ListFeedReturnValue**](SearchV4ListFeedReturnValue.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_query_advisories**
> SearchV4AdvisoryReturnValue v4_query_advisories(name=name, cve_id=cve_id, vendor=vendor, product=product, platform=platform, version=version, cpe=cpe, package_name=package_name, purl=purl, reference_url=reference_url, reference_tag=reference_tag, description_lang=description_lang, updated_after=updated_after, updated_before=updated_before, page=page, limit=limit, start_cursor=start_cursor, cursor=cursor)

Query advisories

Query the VulnCheck v4 advisory index

### Example

* Api Key Authentication (Bearer):

```python
import vulncheck_sdk
from vulncheck_sdk.models.search_v4_advisory_return_value import SearchV4AdvisoryReturnValue
from vulncheck_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.vulncheck.com
# See configuration.py for a list of all supported configuration parameters.
configuration = vulncheck_sdk.Configuration(
    host = "https://api.vulncheck.com"
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
    api_instance = vulncheck_sdk.AdvisoryApi(api_client)
    name = 'name_example' # str | Filter by advisory feed name (e.g. 'vulncheck') (optional)
    cve_id = 'cve_id_example' # str | Filter by CVE ID (e.g. 'CVE-2024-1234') (optional)
    vendor = 'vendor_example' # str | Filter by vendor name (optional)
    product = 'product_example' # str | Filter by product name (optional)
    platform = 'platform_example' # str | Filter by OS/platform (optional)
    version = 'version_example' # str | Filter by product version (semver-aware) (optional)
    cpe = 'cpe_example' # str | Filter by CPE (e.g. 'cpe:2.3:a:vendor:product:*') (optional)
    package_name = 'package_name_example' # str | Filter by package name (optional)
    purl = 'purl_example' # str | Filter by package URL (PURL) (optional)
    reference_url = 'reference_url_example' # str | Filter by reference URL (optional)
    reference_tag = 'reference_tag_example' # str | Filter by reference tag (e.g. 'patch', 'advisory') (optional)
    description_lang = 'description_lang_example' # str | Filter by description language (e.g. 'en') (optional)
    updated_after = 'updated_after_example' # str | Return advisories updated after this date (RFC3339 or date-math e.g. 'now-30d') (optional)
    updated_before = 'updated_before_example' # str | Return advisories updated before this date (RFC3339 or date-math) (optional)
    page = 56 # int | Page number (default: 1) (optional)
    limit = 56 # int | Results per page, max 100 (default: 10) (optional)
    start_cursor = 'start_cursor_example' # str | Presence activates cursor mode from the first page (value is ignored; cannot be combined with page) (optional)
    cursor = 'cursor_example' # str | Cursor from previous response _meta.next_cursor to fetch the next page (optional)

    try:
        # Query advisories
        api_response = api_instance.v4_query_advisories(name=name, cve_id=cve_id, vendor=vendor, product=product, platform=platform, version=version, cpe=cpe, package_name=package_name, purl=purl, reference_url=reference_url, reference_tag=reference_tag, description_lang=description_lang, updated_after=updated_after, updated_before=updated_before, page=page, limit=limit, start_cursor=start_cursor, cursor=cursor)
        print("The response of AdvisoryApi->v4_query_advisories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdvisoryApi->v4_query_advisories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter by advisory feed name (e.g. &#39;vulncheck&#39;) | [optional] 
 **cve_id** | **str**| Filter by CVE ID (e.g. &#39;CVE-2024-1234&#39;) | [optional] 
 **vendor** | **str**| Filter by vendor name | [optional] 
 **product** | **str**| Filter by product name | [optional] 
 **platform** | **str**| Filter by OS/platform | [optional] 
 **version** | **str**| Filter by product version (semver-aware) | [optional] 
 **cpe** | **str**| Filter by CPE (e.g. &#39;cpe:2.3:a:vendor:product:*&#39;) | [optional] 
 **package_name** | **str**| Filter by package name | [optional] 
 **purl** | **str**| Filter by package URL (PURL) | [optional] 
 **reference_url** | **str**| Filter by reference URL | [optional] 
 **reference_tag** | **str**| Filter by reference tag (e.g. &#39;patch&#39;, &#39;advisory&#39;) | [optional] 
 **description_lang** | **str**| Filter by description language (e.g. &#39;en&#39;) | [optional] 
 **updated_after** | **str**| Return advisories updated after this date (RFC3339 or date-math e.g. &#39;now-30d&#39;) | [optional] 
 **updated_before** | **str**| Return advisories updated before this date (RFC3339 or date-math) | [optional] 
 **page** | **int**| Page number (default: 1) | [optional] 
 **limit** | **int**| Results per page, max 100 (default: 10) | [optional] 
 **start_cursor** | **str**| Presence activates cursor mode from the first page (value is ignored; cannot be combined with page) | [optional] 
 **cursor** | **str**| Cursor from previous response _meta.next_cursor to fetch the next page | [optional] 

### Return type

[**SearchV4AdvisoryReturnValue**](SearchV4AdvisoryReturnValue.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**402** | Payment Required |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

