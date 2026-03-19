# SearchErrorResponse

search.ErrorResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **bool** |  | [optional] 
**errors** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.search_error_response import SearchErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SearchErrorResponse from a JSON string
search_error_response_instance = SearchErrorResponse.from_json(json)
# print the JSON string representation of the object
print(SearchErrorResponse.to_json())

# convert the object into a dict
search_error_response_dict = search_error_response_instance.to_dict()
# create an instance of SearchErrorResponse from a dict
search_error_response_from_dict = SearchErrorResponse.from_dict(search_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


