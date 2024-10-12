# AdvisoryVulnCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affecting** | **List[str]** |  | [optional] 
**credit** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss** | **str** |  | [optional] 
**cvss_v3_vector** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**severity** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_vuln_check import AdvisoryVulnCheck

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVulnCheck from a JSON string
advisory_vuln_check_instance = AdvisoryVulnCheck.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVulnCheck.to_json())

# convert the object into a dict
advisory_vuln_check_dict = advisory_vuln_check_instance.to_dict()
# create an instance of AdvisoryVulnCheck from a dict
advisory_vuln_check_from_dict = AdvisoryVulnCheck.from_dict(advisory_vuln_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


