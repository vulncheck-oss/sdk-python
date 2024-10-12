# ApiNVD20WeaknessExtended


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**List[ApiNVD20WeaknessDescExtended]**](ApiNVD20WeaknessDescExtended.md) |  | [optional] 
**source** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_weakness_extended import ApiNVD20WeaknessExtended

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20WeaknessExtended from a JSON string
api_nvd20_weakness_extended_instance = ApiNVD20WeaknessExtended.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20WeaknessExtended.to_json())

# convert the object into a dict
api_nvd20_weakness_extended_dict = api_nvd20_weakness_extended_instance.to_dict()
# create an instance of ApiNVD20WeaknessExtended from a dict
api_nvd20_weakness_extended_from_dict = ApiNVD20WeaknessExtended.from_dict(api_nvd20_weakness_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


