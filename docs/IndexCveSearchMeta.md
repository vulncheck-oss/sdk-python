# IndexCveSearchMeta

Meta is the metadata related to the endpoint response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_count** | **int** | CurrentCount is the number of documents returned in this response. | [optional] 
**cve** | **str** | CVE is the CVE identifier that was searched for. | [optional] 
**indices_with_hits** | **int** | IndicesWithHits is the number of indices that contained at least one match. | [optional] 
**limit** | **int** | Limit is the maximum number of results requested per page. | [optional] 
**next_cursor** | **str** | NextCursor is the cursor for fetching the next page of results. Empty if there are no more results (current_count &lt; limit). | [optional] 
**page** | **int** | Page is the current page number (only set in page-based pagination mode). | [optional] 
**queried_index_count** | **int** | QueriedIndexCount is the number of indices that were searched. | [optional] 
**timestamp** | **str** | Timestamp is the UTC time when the search was executed. | [optional] 
**top_index_counts** | [**List[IndexIndexCountEntry]**](IndexIndexCountEntry.md) | TopIndexCounts contains the top indices by document count (up to 10). | [optional] 
**total_count** | **int** | TotalCount is the total number of matching documents across all queried indices. | [optional] 
**total_pages** | **int** | TotalPages is the total number of pages (only set in page-based pagination mode). | [optional] 

## Example

```python
from vulncheck_sdk.models.index_cve_search_meta import IndexCveSearchMeta

# TODO update the JSON string below
json = "{}"
# create an instance of IndexCveSearchMeta from a JSON string
index_cve_search_meta_instance = IndexCveSearchMeta.from_json(json)
# print the JSON string representation of the object
print(IndexCveSearchMeta.to_json())

# convert the object into a dict
index_cve_search_meta_dict = index_cve_search_meta_instance.to_dict()
# create an instance of IndexCveSearchMeta from a dict
index_cve_search_meta_from_dict = IndexCveSearchMeta.from_dict(index_cve_search_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


