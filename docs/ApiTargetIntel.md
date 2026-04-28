# ApiTargetIntel

api.TargetIntel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional] 
**as_domain** | **str** |  | [optional] 
**as_name** | **str** |  | [optional] 
**asn** | **str** |  | [optional] 
**confidence** | **float** |  | [optional] 
**country** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**cpe** | **str** |  | [optional] 
**cves** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fingerprint_metadata** | **List[int]** |  | [optional] 
**ip** | **str** |  | [optional] 
**match_target** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**product** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**rule_id** | **str** |  | [optional] 
**rule_source** | **str** |  | [optional] 
**service_metadata** | **List[int]** |  | [optional] 
**type** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

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


