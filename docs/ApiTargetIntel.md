# ApiTargetIntel

api.TargetIntel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_domain** | **str** |  | [optional] 
**as_name** | **str** |  | [optional] 
**asn** | **str** |  | [optional] 
**classifications** | **List[str]** |  | [optional] 
**contains_cve** | **bool** |  | [optional] 
**country** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**cpe** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fingerprints** | [**List[ApiFingerprint]**](ApiFingerprint.md) |  | [optional] 
**hostname** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**metadata** | **List[int]** |  | [optional] 
**port** | **int** |  | [optional] 
**product** | **List[str]** |  | [optional] 
**protocol** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 
**vendor** | **List[str]** |  | [optional] 
**version** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_target_intel import ApiTargetIntel

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTargetIntel from a JSON string
api_target_intel_instance = ApiTargetIntel.from_json(json)
# print the JSON string representation of the object
print(ApiTargetIntel.to_json())

# convert the object into a dict
api_target_intel_dict = api_target_intel_instance.to_dict()
# create an instance of ApiTargetIntel from a dict
api_target_intel_from_dict = ApiTargetIntel.from_dict(api_target_intel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


