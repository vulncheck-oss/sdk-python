# ApiUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** | sort // key | [optional] 
**issued** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**os_arch** | **str** |  | [optional] 
**os_version** | **str** |  | [optional] 
**packages** | [**List[ApiPackage]**](ApiPackage.md) |  | [optional] 
**references** | [**List[ApiReference]**](ApiReference.md) |  | [optional] 
**severity** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**updated** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_update import ApiUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUpdate from a JSON string
api_update_instance = ApiUpdate.from_json(json)
# print the JSON string representation of the object
print(ApiUpdate.to_json())

# convert the object into a dict
api_update_dict = api_update_instance.to_dict()
# create an instance of ApiUpdate from a dict
api_update_from_dict = ApiUpdate.from_dict(api_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


