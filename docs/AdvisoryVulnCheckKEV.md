# AdvisoryVulnCheckKEV


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional] 
**cisa_date_added** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**due_date** | **str** |  | [optional] 
**known_ransomware_campaign_use** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**required_action** | **str** |  | [optional] 
**short_description** | **str** |  | [optional] 
**vendor_project** | **str** |  | [optional] 
**vulncheck_reported_exploitation** | [**List[AdvisoryReportedExploit]**](AdvisoryReportedExploit.md) |  | [optional] 
**vulncheck_xdb** | [**List[AdvisoryXDB]**](AdvisoryXDB.md) |  | [optional] 
**vulnerability_name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_vuln_check_kev import AdvisoryVulnCheckKEV

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVulnCheckKEV from a JSON string
advisory_vuln_check_kev_instance = AdvisoryVulnCheckKEV.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVulnCheckKEV.to_json())

# convert the object into a dict
advisory_vuln_check_kev_dict = advisory_vuln_check_kev_instance.to_dict()
# create an instance of AdvisoryVulnCheckKEV from a dict
advisory_vuln_check_kev_from_dict = AdvisoryVulnCheckKEV.from_dict(advisory_vuln_check_kev_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


