# AdvisoryCiscoAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cisco_bug_id** | **str** | multiple | [optional] 
**csaf** | **str** |  | [optional] 
**cve** | **List[str]** | multiple | [optional] 
**cvrf** | **str** |  | [optional] 
**cwe** | **str** | multiple | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**related_resources** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**total_count** | **int** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**workarounds** | **str** |  | [optional] 
**workflow_status** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cisco_advisory import AdvisoryCiscoAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCiscoAdvisory from a JSON string
advisory_cisco_advisory_instance = AdvisoryCiscoAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCiscoAdvisory.to_json())

# convert the object into a dict
advisory_cisco_advisory_dict = advisory_cisco_advisory_instance.to_dict()
# create an instance of AdvisoryCiscoAdvisory from a dict
advisory_cisco_advisory_from_dict = AdvisoryCiscoAdvisory.from_dict(advisory_cisco_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


