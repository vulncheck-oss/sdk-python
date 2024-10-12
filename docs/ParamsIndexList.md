# ParamsIndexList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**href** | **str** | Href API endpoint URI to detailed index information | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.params_index_list import ParamsIndexList

# TODO update the JSON string below
json = "{}"
# create an instance of ParamsIndexList from a JSON string
params_index_list_instance = ParamsIndexList.from_json(json)
# print the JSON string representation of the object
print(ParamsIndexList.to_json())

# convert the object into a dict
params_index_list_dict = params_index_list_instance.to_dict()
# create an instance of ParamsIndexList from a dict
params_index_list_from_dict = ParamsIndexList.from_dict(params_index_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


