# AdvisoryArchIssue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisories** | **List[str]** |  | [optional] 
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **str** |  | [optional] 
**issues** | **List[str]** | cves | [optional] 
**name** | **str** |  | [optional] 
**packages** | **List[str]** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**severity** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**ticket** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_arch_issue import AdvisoryArchIssue

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryArchIssue from a JSON string
advisory_arch_issue_instance = AdvisoryArchIssue.from_json(json)
# print the JSON string representation of the object
print(AdvisoryArchIssue.to_json())

# convert the object into a dict
advisory_arch_issue_dict = advisory_arch_issue_instance.to_dict()
# create an instance of AdvisoryArchIssue from a dict
advisory_arch_issue_from_dict = AdvisoryArchIssue.from_dict(advisory_arch_issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


