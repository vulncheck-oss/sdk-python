# ApiNVD20Weakness


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**List[ApiNVD20Description]**](ApiNVD20Description.md) |  | [optional] 
**source** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_weakness import ApiNVD20Weakness

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20Weakness from a JSON string
api_nvd20_weakness_instance = ApiNVD20Weakness.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20Weakness.to_json())

# convert the object into a dict
api_nvd20_weakness_dict = api_nvd20_weakness_instance.to_dict()
# create an instance of ApiNVD20Weakness from a dict
api_nvd20_weakness_from_dict = ApiNVD20Weakness.from_dict(api_nvd20_weakness_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


