# ApiNVD20DetailsExtended

api.NVD20DetailsExtended

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**new_cwes** | **List[str]** |  | [optional] 
**new_types** | **List[str]** |  | [optional] 
**new_url** | **str** |  | [optional] 
**new_value** | **object** |  | [optional] 
**old_cwes** | **List[str]** |  | [optional] 
**old_types** | **List[str]** |  | [optional] 
**old_url** | **str** |  | [optional] 
**old_value** | **object** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_details_extended import ApiNVD20DetailsExtended

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20DetailsExtended from a JSON string
api_nvd20_details_extended_instance = ApiNVD20DetailsExtended.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20DetailsExtended.to_json())

# convert the object into a dict
api_nvd20_details_extended_dict = api_nvd20_details_extended_instance.to_dict()
# create an instance of ApiNVD20DetailsExtended from a dict
api_nvd20_details_extended_from_dict = ApiNVD20DetailsExtended.from_dict(api_nvd20_details_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


