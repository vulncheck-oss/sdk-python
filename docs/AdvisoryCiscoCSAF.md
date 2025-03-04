# AdvisoryCiscoCSAF


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csaf** | **object** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cisco_csaf import AdvisoryCiscoCSAF

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCiscoCSAF from a JSON string
advisory_cisco_csaf_instance = AdvisoryCiscoCSAF.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCiscoCSAF.to_json())

# convert the object into a dict
advisory_cisco_csaf_dict = advisory_cisco_csaf_instance.to_dict()
# create an instance of AdvisoryCiscoCSAF from a dict
advisory_cisco_csaf_from_dict = AdvisoryCiscoCSAF.from_dict(advisory_cisco_csaf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


