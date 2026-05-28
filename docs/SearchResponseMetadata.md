# SearchResponseMetadata

Meta is the metadata related to the endpoint response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional] 
**total_documents** | **int** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.search_response_metadata import SearchResponseMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResponseMetadata from a JSON string
search_response_metadata_instance = SearchResponseMetadata.from_json(json)
# print the JSON string representation of the object
print(SearchResponseMetadata.to_json())

# convert the object into a dict
search_response_metadata_dict = search_response_metadata_instance.to_dict()
# create an instance of SearchResponseMetadata from a dict
search_response_metadata_from_dict = SearchResponseMetadata.from_dict(search_response_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


