# PaginatePagination

Meta is the metadata related to the endpoint response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **str** | Cursor is an opaque string representing the current page position for cursor-based pagination. Contains encoded information about sort values and position markers. Use this value with the &#39;cursor&#39; query parameter to resume pagination from this point. | [optional] 
**first_item** | **int** | FirstItem is the 1-indexed position of the first item on the current page. Example: Page 1 with limit 100 → FirstItem &#x3D; 1          Page 2 with limit 100 → FirstItem &#x3D; 101 | [optional] 
**index** | **str** | Index name being queried, corresponding to the VulnCheck data feed. Examples: \&quot;exploits\&quot;, \&quot;vulncheck-nvd2\&quot;, \&quot;ipintel-3d\&quot;, \&quot;malicious-vscode-exts\&quot; | [optional] 
**last_item** | **int** | LastItem is the 1-indexed position of the last item on the current page. Accounts for partial pages. Example: Page with 50 items → LastItem &#x3D; FirstItem + 49 On the final page, LastItem equals TotalRows. | [optional] 
**limit** | **int** | Limit is the maximum number of items returned in this response. Range: 1-100 for standard indices, 1-10 for large indices. Default: 100 (or 10 for indices marked as \&quot;large\&quot; in metadata) | [optional] 
**matches** | [**List[PaginateMatch]**](PaginateMatch.md) | Matches shows the active filter values applied to the current query. Each match includes the field name and the value being filtered on. Helps users understand which filters are currently active. | [optional] 
**max_pages** | **int** | MaxPages is the maximum number of pages allowed for offset-based pagination. Performance limit to prevent expensive deep pagination. Default: 6 pages. When TotalPages &gt; MaxPages, cursor-based pagination should be used instead. | [optional] 
**next_cursor** | **str** | NextCursor is an opaque string for fetching the next page in cursor-based pagination. When empty or null, indicates no more pages are available. More efficient than offset pagination for large datasets and real-time data. | [optional] 
**opensearch_query** | **object** | OSQuery contains the raw OpenSearch query JSON used internally. Only included when show_query&#x3D;true parameter is set. Useful for debugging complex queries and understanding performance. | [optional] 
**order** | **str** | Order specifies the sort direction: \&quot;asc\&quot; (ascending) or \&quot;desc\&quot; (descending). Default: \&quot;desc\&quot; for most time-based indices to show newest items first. | [optional] 
**page** | **int** | Page is the current page number for offset-based pagination (1-indexed). First page &#x3D; 1, second page &#x3D; 2, etc. Used with Limit to calculate database offset. For cursor-based pagination, this field may be omitted or estimated. | [optional] 
**pages** | **List[str]** | Pages contains page numbers to display in pagination UI (e.g., [1, 2, \&quot;...\&quot;, 45]). Only populated when ShowPages&#x3D;true. Includes ellipsis (\&quot;...\&quot;) for gaps. Limited by MaxPages to prevent overwhelming UI with too many page links. | [optional] 
**parameters** | [**List[PaginateParam]**](PaginateParam.md) | Params describes available query parameters for this index. Each parameter includes name, format constraints, and filtering capabilities. Used for building dynamic query UIs and input validation. | [optional] 
**show_pages** | **bool** | ShowPages controls whether the Pages array should be calculated and included. Set to true for UI pagination controls, false for API-only usage to save processing. | [optional] 
**show_query** | **bool** | ShowQuery indicates whether the raw OpenSearch query should be included. When true, OSQuery field will be populated with the internal query structure. | [optional] 
**sort** | **str** | Sort field used for ordering results. Available fields vary by index. Common values: \&quot;_timestamp\&quot;, \&quot;date_added\&quot;, \&quot;_id\&quot;, \&quot;lastSeen\&quot; Affects cursor generation and ensures pagination consistency. | [optional] 
**timestamp** | **str** | Timestamp when the query was executed in UTC (ISO 8601 format). Used for debugging, cache management, and determining data freshness. Example: \&quot;2024-02-23T20:35:43.732591251Z\&quot; | [optional] 
**total_documents** | **int** | TotalRows is the total number of documents matching the query across all pages. Used for calculating total_pages and building pagination UI elements. Note: May be capped for performance on very large result sets. | [optional] 
**total_pages** | **int** | TotalPages is the total number of pages based on TotalRows and Limit. Calculated as: ceil(TotalRows / Limit). Used for pagination UI and validation. Example: 1000 items with limit 100 &#x3D; 10 total pages. | [optional] 
**warnings** | **List[str]** | Warnings contains any non-fatal issues encountered during query processing. Examples: deprecated parameters, performance concerns, or data quality notes. | [optional] 

## Example

```python
from vulncheck_sdk.models.paginate_pagination import PaginatePagination

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatePagination from a JSON string
paginate_pagination_instance = PaginatePagination.from_json(json)
# print the JSON string representation of the object
print(PaginatePagination.to_json())

# convert the object into a dict
paginate_pagination_dict = paginate_pagination_instance.to_dict()
# create an instance of PaginatePagination from a dict
paginate_pagination_from_dict = PaginatePagination.from_dict(paginate_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


