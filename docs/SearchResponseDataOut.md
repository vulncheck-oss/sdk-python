# SearchResponseDataOut

search.ResponseDataOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpe** | **str** |  | [optional] 
**cpe_struct** | [**ApiCPE**](ApiCPE.md) |  | [optional] 
**cves** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.search_response_data_out import SearchResponseDataOut

# TODO update the JSON string below
json = "{}"
# create an instance of SearchResponseDataOut from a JSON string
search_response_data_out_instance = SearchResponseDataOut.from_json(json)
# print the JSON string representation of the object
print(SearchResponseDataOut.to_json())

# convert the object into a dict
search_response_data_out_dict = search_response_data_out_instance.to_dict()
# create an instance of SearchResponseDataOut from a dict
search_response_data_out_from_dict = SearchResponseDataOut.from_dict(search_response_data_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


