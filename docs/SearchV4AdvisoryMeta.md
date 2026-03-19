# SearchV4AdvisoryMeta

search.V4AdvisoryMeta

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **str** |  | [optional] 
**filtered** | **int** |  | [optional] 
**limit** | **int** |  | [optional] 
**next_cursor** | **str** |  | [optional] 
**page** | **int** |  | [optional] 
**pages** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.search_v4_advisory_meta import SearchV4AdvisoryMeta

# TODO update the JSON string below
json = "{}"
# create an instance of SearchV4AdvisoryMeta from a JSON string
search_v4_advisory_meta_instance = SearchV4AdvisoryMeta.from_json(json)
# print the JSON string representation of the object
print(SearchV4AdvisoryMeta.to_json())

# convert the object into a dict
search_v4_advisory_meta_dict = search_v4_advisory_meta_instance.to_dict()
# create an instance of SearchV4AdvisoryMeta from a dict
search_v4_advisory_meta_from_dict = SearchV4AdvisoryMeta.from_dict(search_v4_advisory_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


