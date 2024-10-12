# AdvisoryRedhatCVE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisories** | **List[str]** |  | [optional] 
**advisory_csaf_vex_url** | **List[str]** |  | [optional] 
**affected_packages** | **List[str]** | used for un-marshlling from redhat | [optional] 
**affected_release** | [**List[AdvisoryAffectedRel]**](AdvisoryAffectedRel.md) |  | [optional] 
**bugzilla** | **str** |  | [optional] 
**bugzilla_description** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cve_csaf_vex_url** | **str** |  | [optional] 
**cvss3_score** | **str** |  | [optional] 
**cvss3_scoring_vector** | **str** |  | [optional] 
**cvss_score** | **float** |  | [optional] 
**cvss_scoring_vector** | **str** |  | [optional] 
**cwe** | **str** |  | [optional] 
**package_state** | [**List[AdvisoryPackageStat]**](AdvisoryPackageStat.md) |  | [optional] 
**packages** | [**List[AdvisoryVulnCheckPackage]**](AdvisoryVulnCheckPackage.md) | used to index into vulncheck OS | [optional] 
**public_date** | **str** |  | [optional] 
**resource_url** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_redhat_cve import AdvisoryRedhatCVE

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRedhatCVE from a JSON string
advisory_redhat_cve_instance = AdvisoryRedhatCVE.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRedhatCVE.to_json())

# convert the object into a dict
advisory_redhat_cve_dict = advisory_redhat_cve_instance.to_dict()
# create an instance of AdvisoryRedhatCVE from a dict
advisory_redhat_cve_from_dict = AdvisoryRedhatCVE.from_dict(advisory_redhat_cve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


