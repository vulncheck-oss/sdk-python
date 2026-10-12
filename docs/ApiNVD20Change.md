# ApiNVD20Change

api.NVD20Change

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **str** |  | [optional] 
**cve_change_id** | **str** |  | [optional] 
**cve_id** | **str** |  | [optional] 
**details** | [**List[ApiNVD20DetailsExtended]**](ApiNVD20DetailsExtended.md) |  | [optional] 
**event_name** | **str** |  | [optional] 
**source_identifier** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_change import ApiNVD20Change

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20Change from a JSON string
api_nvd20_change_instance = ApiNVD20Change.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20Change.to_json())

# convert the object into a dict
api_nvd20_change_dict = api_nvd20_change_instance.to_dict()
# create an instance of ApiNVD20Change from a dict
api_nvd20_change_from_dict = ApiNVD20Change.from_dict(api_nvd20_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


