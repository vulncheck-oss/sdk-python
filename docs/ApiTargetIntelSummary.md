# ApiTargetIntelSummary

Summary is a pre-computed rollup of the CVE/fingerprint data above.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmed_count** | **int** |  | [optional] 
**contains_cve** | **bool** |  | [optional] 
**cve_count** | **int** |  | [optional] 
**fingerprint_count** | **int** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_target_intel_summary import ApiTargetIntelSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTargetIntelSummary from a JSON string
api_target_intel_summary_instance = ApiTargetIntelSummary.from_json(json)
# print the JSON string representation of the object
print(ApiTargetIntelSummary.to_json())

# convert the object into a dict
api_target_intel_summary_dict = api_target_intel_summary_instance.to_dict()
# create an instance of ApiTargetIntelSummary from a dict
api_target_intel_summary_from_dict = ApiTargetIntelSummary.from_dict(api_target_intel_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


