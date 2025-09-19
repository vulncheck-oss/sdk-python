# AdvisoryGHAdvisoryJSONLean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss** | [**AdvisoryGHCvss**](AdvisoryGHCvss.md) |  | [optional] 
**cwes** | [**AdvisoryCwes**](AdvisoryCwes.md) |  | [optional] 
**database_id** | **int** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**ghsa_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**identifiers** | [**List[AdvisoryGHIdentifier]**](AdvisoryGHIdentifier.md) |  | [optional] 
**notifications_permalink** | **str** |  | [optional] 
**origin** | **str** |  | [optional] 
**permalink** | **str** |  | [optional] 
**published_at** | **str** |  | [optional] 
**references** | [**List[AdvisoryGHReference]**](AdvisoryGHReference.md) |  | [optional] 
**severity** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**vulnerabilities** | [**AdvisoryGHVulnerabilities**](AdvisoryGHVulnerabilities.md) |  | [optional] 
**withdrawn_at** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_gh_advisory_json_lean import AdvisoryGHAdvisoryJSONLean

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGHAdvisoryJSONLean from a JSON string
advisory_gh_advisory_json_lean_instance = AdvisoryGHAdvisoryJSONLean.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGHAdvisoryJSONLean.to_json())

# convert the object into a dict
advisory_gh_advisory_json_lean_dict = advisory_gh_advisory_json_lean_instance.to_dict()
# create an instance of AdvisoryGHAdvisoryJSONLean from a dict
advisory_gh_advisory_json_lean_from_dict = AdvisoryGHAdvisoryJSONLean.from_dict(advisory_gh_advisory_json_lean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


