# ApiNVD20Description


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lang** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_description import ApiNVD20Description

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20Description from a JSON string
api_nvd20_description_instance = ApiNVD20Description.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20Description.to_json())

# convert the object into a dict
api_nvd20_description_dict = api_nvd20_description_instance.to_dict()
# create an instance of ApiNVD20Description from a dict
api_nvd20_description_from_dict = ApiNVD20Description.from_dict(api_nvd20_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


