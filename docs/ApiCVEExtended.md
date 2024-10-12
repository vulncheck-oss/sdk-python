# ApiCVEExtended


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve_data_meta** | [**ApiCVEDataMetaExtended**](ApiCVEDataMetaExtended.md) |  | [optional] 
**categorization** | [**ApiCategorizationExtended**](ApiCategorizationExtended.md) |  | [optional] 
**data_format** | **str** |  | [optional] 
**data_type** | **str** |  | [optional] 
**data_version** | **str** |  | [optional] 
**description** | [**ApiDescription**](ApiDescription.md) |  | [optional] 
**problemtype** | [**ApiProblemTypeExtended**](ApiProblemTypeExtended.md) |  | [optional] 
**references** | [**ApiReferencesExtended**](ApiReferencesExtended.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_cve_extended import ApiCVEExtended

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCVEExtended from a JSON string
api_cve_extended_instance = ApiCVEExtended.from_json(json)
# print the JSON string representation of the object
print(ApiCVEExtended.to_json())

# convert the object into a dict
api_cve_extended_dict = api_cve_extended_instance.to_dict()
# create an instance of ApiCVEExtended from a dict
api_cve_extended_from_dict = ApiCVEExtended.from_dict(api_cve_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


