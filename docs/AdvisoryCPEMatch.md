# AdvisoryCPEMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria** | **str** |  | [optional] 
**match_criteria_id** | **str** |  | [optional] 
**vulnerable** | **bool** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cpe_match import AdvisoryCPEMatch

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCPEMatch from a JSON string
advisory_cpe_match_instance = AdvisoryCPEMatch.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCPEMatch.to_json())

# convert the object into a dict
advisory_cpe_match_dict = advisory_cpe_match_instance.to_dict()
# create an instance of AdvisoryCPEMatch from a dict
advisory_cpe_match_from_dict = AdvisoryCPEMatch.from_dict(advisory_cpe_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


