# vulncheck_sdk.NvdApi

All URIs are relative to *https://api.vulncheck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nvd_cpe_match_get**](NvdApi.md#nvd_cpe_match_get) | **GET** /rest/json/cpematch/2.0 | Search CPE match criteria (NVD API 2.0 compatible)
[**nvd_cpes_get**](NvdApi.md#nvd_cpes_get) | **GET** /rest/json/cpes/2.0 | Search the CPE dictionary (NVD API 2.0 compatible)
[**nvd_cve_history_get**](NvdApi.md#nvd_cve_history_get) | **GET** /rest/json/cvehistory/2.0 | Search CVE change history (NVD API 2.0 compatible)
[**nvd_cves_get**](NvdApi.md#nvd_cves_get) | **GET** /rest/json/cves/2.0 | Search CVEs (NVD API 2.0 compatible)
[**nvd_source_get**](NvdApi.md#nvd_source_get) | **GET** /rest/json/source/2.0 | List data sources (NVD API 2.0 compatible)


# **nvd_cpe_match_get**
> RestNvdCpeMatchResponse nvd_cpe_match_get(cve_id=cve_id, match_criteria_id=match_criteria_id, last_mod_start_date=last_mod_start_date, last_mod_end_date=last_mod_end_date, results_per_page=results_per_page, start_index=start_index, cursor=cursor)

Search CPE match criteria (NVD API 2.0 compatible)

NVD API 2.0 compatible CPE match criteria search, mirroring NVD's GET /rest/json/cpematch/2.0.

Not yet supported, and rejected with a 400 naming the parameter: matchStringSearch.

### Example

* Api Key Authentication (Bearer):

```python
import vulncheck_sdk
from vulncheck_sdk.models.rest_nvd_cpe_match_response import RestNvdCpeMatchResponse
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
    api_instance = vulncheck_sdk.NvdApi(api_client)
    cve_id = 'cve_id_example' # str | Only match criteria referenced by this CVE's configurations, e.g. CVE-2021-44228 (optional)
    match_criteria_id = 'match_criteria_id_example' # str | A single match criteria by its NVD UUID (optional)
    last_mod_start_date = 'last_mod_start_date_example' # str | Last modified on or after, ISO-8601 (e.g. 2026-01-01T00:00:00.000). Requires lastModEndDate; range at most 120 days (optional)
    last_mod_end_date = 'last_mod_end_date_example' # str | Last modified on or before, ISO-8601. Requires lastModStartDate (optional)
    results_per_page = 500 # int | Page size (optional) (default to 500)
    start_index = 0 # int | Zero-based offset of the first result. Must not be combined with a non-empty cursor (optional) (default to 0)
    cursor = 'cursor_example' # str | VulnCheck extension: opt in to cursor paging. Send it empty for the first page, then the previous response's nextCursor. Responses carry nextCursor only when this is sent (optional)

    try:
        # Search CPE match criteria (NVD API 2.0 compatible)
        api_response = api_instance.nvd_cpe_match_get(cve_id=cve_id, match_criteria_id=match_criteria_id, last_mod_start_date=last_mod_start_date, last_mod_end_date=last_mod_end_date, results_per_page=results_per_page, start_index=start_index, cursor=cursor)
        print("The response of NvdApi->nvd_cpe_match_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NvdApi->nvd_cpe_match_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cve_id** | **str**| Only match criteria referenced by this CVE&#39;s configurations, e.g. CVE-2021-44228 | [optional] 
 **match_criteria_id** | **str**| A single match criteria by its NVD UUID | [optional] 
 **last_mod_start_date** | **str**| Last modified on or after, ISO-8601 (e.g. 2026-01-01T00:00:00.000). Requires lastModEndDate; range at most 120 days | [optional] 
 **last_mod_end_date** | **str**| Last modified on or before, ISO-8601. Requires lastModStartDate | [optional] 
 **results_per_page** | **int**| Page size | [optional] [default to 500]
 **start_index** | **int**| Zero-based offset of the first result. Must not be combined with a non-empty cursor | [optional] [default to 0]
 **cursor** | **str**| VulnCheck extension: opt in to cursor paging. Send it empty for the first page, then the previous response&#39;s nextCursor. Responses carry nextCursor only when this is sent | [optional] 

### Return type

[**RestNvdCpeMatchResponse**](RestNvdCpeMatchResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nvd_cpes_get**
> RestNvdCpesResponse nvd_cpes_get(cpe_name_id=cpe_name_id, cpe_match_string=cpe_match_string, match_criteria_id=match_criteria_id, last_mod_start_date=last_mod_start_date, last_mod_end_date=last_mod_end_date, results_per_page=results_per_page, start_index=start_index, cursor=cursor)

Search the CPE dictionary (NVD API 2.0 compatible)

NVD API 2.0 compatible CPE dictionary search, mirroring NVD's GET /rest/json/cpes/2.0.

Not yet supported, and rejected with a 400 naming the parameter: keywordSearch, keywordExactMatch.

### Example

* Api Key Authentication (Bearer):

```python
import vulncheck_sdk
from vulncheck_sdk.models.rest_nvd_cpes_response import RestNvdCpesResponse
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
    api_instance = vulncheck_sdk.NvdApi(api_client)
    cpe_name_id = 'cpe_name_id_example' # str | A single dictionary entry by its NVD UUID (optional)
    cpe_match_string = 'cpe_match_string_example' # str | A CPE 2.3 name or prefix, e.g. cpe:2.3:a:apache:log4j. CPE 2.2 URIs are not supported (optional)
    match_criteria_id = 'match_criteria_id_example' # str | Only the CPE names this match criteria UUID resolves to (optional)
    last_mod_start_date = 'last_mod_start_date_example' # str | Last modified on or after, ISO-8601 (e.g. 2026-01-01T00:00:00.000). Requires lastModEndDate; range at most 120 days (optional)
    last_mod_end_date = 'last_mod_end_date_example' # str | Last modified on or before, ISO-8601. Requires lastModStartDate (optional)
    results_per_page = 10000 # int | Page size (optional) (default to 10000)
    start_index = 0 # int | Zero-based offset of the first result. Must not be combined with a non-empty cursor (optional) (default to 0)
    cursor = 'cursor_example' # str | VulnCheck extension: opt in to cursor paging. Send it empty for the first page, then the previous response's nextCursor. Responses carry nextCursor only when this is sent (optional)

    try:
        # Search the CPE dictionary (NVD API 2.0 compatible)
        api_response = api_instance.nvd_cpes_get(cpe_name_id=cpe_name_id, cpe_match_string=cpe_match_string, match_criteria_id=match_criteria_id, last_mod_start_date=last_mod_start_date, last_mod_end_date=last_mod_end_date, results_per_page=results_per_page, start_index=start_index, cursor=cursor)
        print("The response of NvdApi->nvd_cpes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NvdApi->nvd_cpes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cpe_name_id** | **str**| A single dictionary entry by its NVD UUID | [optional] 
 **cpe_match_string** | **str**| A CPE 2.3 name or prefix, e.g. cpe:2.3:a:apache:log4j. CPE 2.2 URIs are not supported | [optional] 
 **match_criteria_id** | **str**| Only the CPE names this match criteria UUID resolves to | [optional] 
 **last_mod_start_date** | **str**| Last modified on or after, ISO-8601 (e.g. 2026-01-01T00:00:00.000). Requires lastModEndDate; range at most 120 days | [optional] 
 **last_mod_end_date** | **str**| Last modified on or before, ISO-8601. Requires lastModStartDate | [optional] 
 **results_per_page** | **int**| Page size | [optional] [default to 10000]
 **start_index** | **int**| Zero-based offset of the first result. Must not be combined with a non-empty cursor | [optional] [default to 0]
 **cursor** | **str**| VulnCheck extension: opt in to cursor paging. Send it empty for the first page, then the previous response&#39;s nextCursor. Responses carry nextCursor only when this is sent | [optional] 

### Return type

[**RestNvdCpesResponse**](RestNvdCpesResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nvd_cve_history_get**
> RestNvdCveHistoryResponse nvd_cve_history_get(cve_id=cve_id, event_name=event_name, change_start_date=change_start_date, change_end_date=change_end_date, results_per_page=results_per_page, start_index=start_index, cursor=cursor)

Search CVE change history (NVD API 2.0 compatible)

NVD API 2.0 compatible CVE change history, mirroring NVD's GET /rest/json/cvehistory/2.0.

### Example

* Api Key Authentication (Bearer):

```python
import vulncheck_sdk
from vulncheck_sdk.models.rest_nvd_cve_history_response import RestNvdCveHistoryResponse
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
    api_instance = vulncheck_sdk.NvdApi(api_client)
    cve_id = 'cve_id_example' # str | Only changes to this CVE, e.g. CVE-2021-44228 (optional)
    event_name = 'event_name_example' # str | Only changes of this type. One value per request (optional)
    change_start_date = 'change_start_date_example' # str | Changed on or after, ISO-8601 (e.g. 2026-01-01T00:00:00.000). Requires changeEndDate; range at most 120 days (optional)
    change_end_date = 'change_end_date_example' # str | Changed on or before, ISO-8601. Requires changeStartDate (optional)
    results_per_page = 5000 # int | Page size (optional) (default to 5000)
    start_index = 0 # int | Zero-based offset of the first result. Must not be combined with a non-empty cursor (optional) (default to 0)
    cursor = 'cursor_example' # str | VulnCheck extension: opt in to cursor paging. Send it empty for the first page, then the previous response's nextCursor. Responses carry nextCursor only when this is sent (optional)

    try:
        # Search CVE change history (NVD API 2.0 compatible)
        api_response = api_instance.nvd_cve_history_get(cve_id=cve_id, event_name=event_name, change_start_date=change_start_date, change_end_date=change_end_date, results_per_page=results_per_page, start_index=start_index, cursor=cursor)
        print("The response of NvdApi->nvd_cve_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NvdApi->nvd_cve_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cve_id** | **str**| Only changes to this CVE, e.g. CVE-2021-44228 | [optional] 
 **event_name** | **str**| Only changes of this type. One value per request | [optional] 
 **change_start_date** | **str**| Changed on or after, ISO-8601 (e.g. 2026-01-01T00:00:00.000). Requires changeEndDate; range at most 120 days | [optional] 
 **change_end_date** | **str**| Changed on or before, ISO-8601. Requires changeStartDate | [optional] 
 **results_per_page** | **int**| Page size | [optional] [default to 5000]
 **start_index** | **int**| Zero-based offset of the first result. Must not be combined with a non-empty cursor | [optional] [default to 0]
 **cursor** | **str**| VulnCheck extension: opt in to cursor paging. Send it empty for the first page, then the previous response&#39;s nextCursor. Responses carry nextCursor only when this is sent | [optional] 

### Return type

[**RestNvdCveHistoryResponse**](RestNvdCveHistoryResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nvd_cves_get**
> RestNvdCvesResponse nvd_cves_get(cve_id=cve_id, cve_ids=cve_ids, cpe_name=cpe_name, is_vulnerable=is_vulnerable, virtual_match_string=virtual_match_string, version_start=version_start, version_start_type=version_start_type, version_end=version_end, version_end_type=version_end_type, vuln_statuses=vuln_statuses, cve_tag=cve_tag, no_rejected=no_rejected, has_kev=has_kev, vc_vulnerable_cpes=vc_vulnerable_cpes, pub_start_date=pub_start_date, pub_end_date=pub_end_date, last_mod_start_date=last_mod_start_date, last_mod_end_date=last_mod_end_date, source_identifier=source_identifier, results_per_page=results_per_page, start_index=start_index, cursor=cursor)

Search CVEs (NVD API 2.0 compatible)

NVD API 2.0 compatible CVE search, mirroring NVD's GET /rest/json/cves/2.0. Each record also carries VulnCheck's vcConfigurations.

Not yet supported, and rejected with a 400 naming the parameter: keywordSearch, keywordExactMatch, cvssV2Metrics, cvssV2Severity, cvssV3Metrics, cvssV3Severity, cvssV4Metrics, cvssV4Severity, cweId, hasCertAlerts, hasCertNotes, hasOval, kevStartDate, kevEndDate.

### Example

* Api Key Authentication (Bearer):

```python
import vulncheck_sdk
from vulncheck_sdk.models.rest_nvd_cves_response import RestNvdCvesResponse
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
    api_instance = vulncheck_sdk.NvdApi(api_client)
    cve_id = 'cve_id_example' # str | A single CVE ID, e.g. CVE-2021-44228 (optional)
    cve_ids = 'cve_ids_example' # str | Comma-separated CVE IDs, at most 100 (optional)
    cpe_name = 'cpe_name_example' # str | A complete CPE 2.3 name; returns CVEs whose configurations match it. Takes precedence over virtualMatchString (optional)
    is_vulnerable = True # bool | Only CVEs where cpeName is marked vulnerable. Requires cpeName (optional)
    virtual_match_string = 'virtual_match_string_example' # str | A CPE 2.3 name or prefix (at least part and vendor) matched against configuration criteria (optional)
    version_start = 'version_start_example' # str | Lower version bound. Requires virtualMatchString and versionStartType (optional)
    version_start_type = 'version_start_type_example' # str | Whether versionStart is inclusive. Requires versionStart (optional)
    version_end = 'version_end_example' # str | Upper version bound. Requires virtualMatchString and versionEndType (optional)
    version_end_type = 'version_end_type_example' # str | Whether versionEnd is inclusive. Requires versionEnd (optional)
    vuln_statuses = 'vuln_statuses_example' # str | Comma-separated vulnStatus values: UndergoingAnalysis, Modified, AwaitingAnalysis, Rejected, Received, Analyzed, Deferred (optional)
    cve_tag = 'cve_tag_example' # str | Only CVEs carrying this tag (optional)
    no_rejected = True # bool | Exclude rejected CVEs (optional)
    has_kev = True # bool | Only CVEs in the CISA KEV catalog (optional)
    vc_vulnerable_cpes = True # bool | VulnCheck extension: include the flat vcVulnerableCPEs list on each record. Off by default; it can be most of a page's size (optional)
    pub_start_date = 'pub_start_date_example' # str | Published on or after, ISO-8601 (e.g. 2026-01-01T00:00:00.000). Requires pubEndDate; range at most 120 days (optional)
    pub_end_date = 'pub_end_date_example' # str | Published on or before, ISO-8601. Requires pubStartDate (optional)
    last_mod_start_date = 'last_mod_start_date_example' # str | Last modified on or after, ISO-8601. Requires lastModEndDate; range at most 120 days (optional)
    last_mod_end_date = 'last_mod_end_date_example' # str | Last modified on or before, ISO-8601. Requires lastModStartDate (optional)
    source_identifier = 'source_identifier_example' # str | Only CVEs from this source, e.g. cve@mitre.org (optional)
    results_per_page = 2000 # int | Page size (optional) (default to 2000)
    start_index = 0 # int | Zero-based offset of the first result. Must not be combined with a non-empty cursor (optional) (default to 0)
    cursor = 'cursor_example' # str | VulnCheck extension: opt in to cursor paging. Send it empty for the first page, then the previous response's nextCursor. Responses carry nextCursor only when this is sent (optional)

    try:
        # Search CVEs (NVD API 2.0 compatible)
        api_response = api_instance.nvd_cves_get(cve_id=cve_id, cve_ids=cve_ids, cpe_name=cpe_name, is_vulnerable=is_vulnerable, virtual_match_string=virtual_match_string, version_start=version_start, version_start_type=version_start_type, version_end=version_end, version_end_type=version_end_type, vuln_statuses=vuln_statuses, cve_tag=cve_tag, no_rejected=no_rejected, has_kev=has_kev, vc_vulnerable_cpes=vc_vulnerable_cpes, pub_start_date=pub_start_date, pub_end_date=pub_end_date, last_mod_start_date=last_mod_start_date, last_mod_end_date=last_mod_end_date, source_identifier=source_identifier, results_per_page=results_per_page, start_index=start_index, cursor=cursor)
        print("The response of NvdApi->nvd_cves_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NvdApi->nvd_cves_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cve_id** | **str**| A single CVE ID, e.g. CVE-2021-44228 | [optional] 
 **cve_ids** | **str**| Comma-separated CVE IDs, at most 100 | [optional] 
 **cpe_name** | **str**| A complete CPE 2.3 name; returns CVEs whose configurations match it. Takes precedence over virtualMatchString | [optional] 
 **is_vulnerable** | **bool**| Only CVEs where cpeName is marked vulnerable. Requires cpeName | [optional] 
 **virtual_match_string** | **str**| A CPE 2.3 name or prefix (at least part and vendor) matched against configuration criteria | [optional] 
 **version_start** | **str**| Lower version bound. Requires virtualMatchString and versionStartType | [optional] 
 **version_start_type** | **str**| Whether versionStart is inclusive. Requires versionStart | [optional] 
 **version_end** | **str**| Upper version bound. Requires virtualMatchString and versionEndType | [optional] 
 **version_end_type** | **str**| Whether versionEnd is inclusive. Requires versionEnd | [optional] 
 **vuln_statuses** | **str**| Comma-separated vulnStatus values: UndergoingAnalysis, Modified, AwaitingAnalysis, Rejected, Received, Analyzed, Deferred | [optional] 
 **cve_tag** | **str**| Only CVEs carrying this tag | [optional] 
 **no_rejected** | **bool**| Exclude rejected CVEs | [optional] 
 **has_kev** | **bool**| Only CVEs in the CISA KEV catalog | [optional] 
 **vc_vulnerable_cpes** | **bool**| VulnCheck extension: include the flat vcVulnerableCPEs list on each record. Off by default; it can be most of a page&#39;s size | [optional] 
 **pub_start_date** | **str**| Published on or after, ISO-8601 (e.g. 2026-01-01T00:00:00.000). Requires pubEndDate; range at most 120 days | [optional] 
 **pub_end_date** | **str**| Published on or before, ISO-8601. Requires pubStartDate | [optional] 
 **last_mod_start_date** | **str**| Last modified on or after, ISO-8601. Requires lastModEndDate; range at most 120 days | [optional] 
 **last_mod_end_date** | **str**| Last modified on or before, ISO-8601. Requires lastModStartDate | [optional] 
 **source_identifier** | **str**| Only CVEs from this source, e.g. cve@mitre.org | [optional] 
 **results_per_page** | **int**| Page size | [optional] [default to 2000]
 **start_index** | **int**| Zero-based offset of the first result. Must not be combined with a non-empty cursor | [optional] [default to 0]
 **cursor** | **str**| VulnCheck extension: opt in to cursor paging. Send it empty for the first page, then the previous response&#39;s nextCursor. Responses carry nextCursor only when this is sent | [optional] 

### Return type

[**RestNvdCvesResponse**](RestNvdCvesResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nvd_source_get**
> RestNvdSourceResponse nvd_source_get(source_identifier=source_identifier, last_mod_start_date=last_mod_start_date, last_mod_end_date=last_mod_end_date, results_per_page=results_per_page, start_index=start_index)

List data sources (NVD API 2.0 compatible)

NVD API 2.0 compatible source list, mirroring NVD's GET /rest/json/source/2.0. Unlike the other endpoints it has no cursor paging.

### Example

* Api Key Authentication (Bearer):

```python
import vulncheck_sdk
from vulncheck_sdk.models.rest_nvd_source_response import RestNvdSourceResponse
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
    api_instance = vulncheck_sdk.NvdApi(api_client)
    source_identifier = 'source_identifier_example' # str | Only the source with this identifier, e.g. cve@mitre.org (optional)
    last_mod_start_date = 'last_mod_start_date_example' # str | Last modified on or after, ISO-8601 (e.g. 2026-01-01T00:00:00.000). Requires lastModEndDate; range at most 120 days (optional)
    last_mod_end_date = 'last_mod_end_date_example' # str | Last modified on or before, ISO-8601. Requires lastModStartDate (optional)
    results_per_page = 1000 # int | Page size (optional) (default to 1000)
    start_index = 0 # int | Zero-based offset of the first result (optional) (default to 0)

    try:
        # List data sources (NVD API 2.0 compatible)
        api_response = api_instance.nvd_source_get(source_identifier=source_identifier, last_mod_start_date=last_mod_start_date, last_mod_end_date=last_mod_end_date, results_per_page=results_per_page, start_index=start_index)
        print("The response of NvdApi->nvd_source_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NvdApi->nvd_source_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_identifier** | **str**| Only the source with this identifier, e.g. cve@mitre.org | [optional] 
 **last_mod_start_date** | **str**| Last modified on or after, ISO-8601 (e.g. 2026-01-01T00:00:00.000). Requires lastModEndDate; range at most 120 days | [optional] 
 **last_mod_end_date** | **str**| Last modified on or before, ISO-8601. Requires lastModStartDate | [optional] 
 **results_per_page** | **int**| Page size | [optional] [default to 1000]
 **start_index** | **int**| Zero-based offset of the first result | [optional] [default to 0]

### Return type

[**RestNvdSourceResponse**](RestNvdSourceResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

