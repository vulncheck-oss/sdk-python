# ApiTargetIntelCVESummary

api.TargetIntelCVESummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional] 
**asns** | [**List[ApiTargetIntelCVESummaryAsnsInner]**](ApiTargetIntelCVESummaryAsnsInner.md) |  | [optional] 
**country_codes** | [**List[ApiTargetIntelCVESummaryAsnsInner]**](ApiTargetIntelCVESummaryAsnsInner.md) |  | [optional] 
**cve** | **str** |  | [optional] 
**ports** | [**List[ApiTargetIntelCVESummaryPortsInner]**](ApiTargetIntelCVESummaryPortsInner.md) |  | [optional] 
**vendors** | [**List[ApiTargetIntelCVESummaryAsnsInner]**](ApiTargetIntelCVESummaryAsnsInner.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_target_intel_cve_summary import ApiTargetIntelCVESummary

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTargetIntelCVESummary from a JSON string
api_target_intel_cve_summary_instance = ApiTargetIntelCVESummary.from_json(json)
# print the JSON string representation of the object
print(ApiTargetIntelCVESummary.to_json())

# convert the object into a dict
api_target_intel_cve_summary_dict = api_target_intel_cve_summary_instance.to_dict()
# create an instance of ApiTargetIntelCVESummary from a dict
api_target_intel_cve_summary_from_dict = ApiTargetIntelCVESummary.from_dict(api_target_intel_cve_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


