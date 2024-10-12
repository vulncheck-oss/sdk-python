# ApiNVD20ReferenceExtended


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_added** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**lang** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**previous_url** | **str** |  | [optional] 
**refsource** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_reference_extended import ApiNVD20ReferenceExtended

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20ReferenceExtended from a JSON string
api_nvd20_reference_extended_instance = ApiNVD20ReferenceExtended.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20ReferenceExtended.to_json())

# convert the object into a dict
api_nvd20_reference_extended_dict = api_nvd20_reference_extended_instance.to_dict()
# create an instance of ApiNVD20ReferenceExtended from a dict
api_nvd20_reference_extended_from_dict = ApiNVD20ReferenceExtended.from_dict(api_nvd20_reference_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


