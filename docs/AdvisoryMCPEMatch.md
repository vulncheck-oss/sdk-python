# AdvisoryMCPEMatch


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
from vulncheck_sdk.models.advisory_mcpe_match import AdvisoryMCPEMatch

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMCPEMatch from a JSON string
advisory_mcpe_match_instance = AdvisoryMCPEMatch.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMCPEMatch.to_json())

# convert the object into a dict
advisory_mcpe_match_dict = advisory_mcpe_match_instance.to_dict()
# create an instance of AdvisoryMCPEMatch from a dict
advisory_mcpe_match_from_dict = AdvisoryMCPEMatch.from_dict(advisory_mcpe_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


