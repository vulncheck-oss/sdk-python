# AdvisoryNVD20CVECPEMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria** | **str** |  | [optional] 
**match_criteria_id** | **str** |  | [optional] 
**version_end_excluding** | **str** |  | [optional] 
**version_end_including** | **str** |  | [optional] 
**version_start_excluding** | **str** |  | [optional] 
**version_start_including** | **str** |  | [optional] 
**vulnerable** | **bool** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_nvd20_cvecpe_match import AdvisoryNVD20CVECPEMatch

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNVD20CVECPEMatch from a JSON string
advisory_nvd20_cvecpe_match_instance = AdvisoryNVD20CVECPEMatch.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNVD20CVECPEMatch.to_json())

# convert the object into a dict
advisory_nvd20_cvecpe_match_dict = advisory_nvd20_cvecpe_match_instance.to_dict()
# create an instance of AdvisoryNVD20CVECPEMatch from a dict
advisory_nvd20_cvecpe_match_from_dict = AdvisoryNVD20CVECPEMatch.from_dict(advisory_nvd20_cvecpe_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


