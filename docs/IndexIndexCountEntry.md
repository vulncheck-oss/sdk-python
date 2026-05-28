# IndexIndexCountEntry

index.IndexCountEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_count** | **int** | DocCount is the number of matching documents in this index. | [optional] 
**index** | **str** | Index is the name of the index. | [optional] 

## Example

```python
from vulncheck_sdk.models.index_index_count_entry import IndexIndexCountEntry

# TODO update the JSON string below
json = "{}"
# create an instance of IndexIndexCountEntry from a JSON string
index_index_count_entry_instance = IndexIndexCountEntry.from_json(json)
# print the JSON string representation of the object
print(IndexIndexCountEntry.to_json())

# convert the object into a dict
index_index_count_entry_dict = index_index_count_entry_instance.to_dict()
# create an instance of IndexIndexCountEntry from a dict
index_index_count_entry_from_dict = IndexIndexCountEntry.from_dict(index_index_count_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


