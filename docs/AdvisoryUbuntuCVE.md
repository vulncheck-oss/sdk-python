# AdvisoryUbuntuCVE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_packages** | [**List[AdvisoryAffectedUbuntuPackage]**](AdvisoryAffectedUbuntuPackage.md) |  | [optional] 
**cve** | **List[str]** | Candidate | [optional] 
**date_added** | **str** | PublicDate | [optional] 
**reference_urls** | **List[str]** | References | [optional] 
**source_url** | **str** |  | [optional] 
**status** | **str** | active || retired | [optional] 
**ubuntu_url** | **str** |  | [optional] 
**usn** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ubuntu_cve import AdvisoryUbuntuCVE

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryUbuntuCVE from a JSON string
advisory_ubuntu_cve_instance = AdvisoryUbuntuCVE.from_json(json)
# print the JSON string representation of the object
print(AdvisoryUbuntuCVE.to_json())

# convert the object into a dict
advisory_ubuntu_cve_dict = advisory_ubuntu_cve_instance.to_dict()
# create an instance of AdvisoryUbuntuCVE from a dict
advisory_ubuntu_cve_from_dict = AdvisoryUbuntuCVE.from_dict(advisory_ubuntu_cve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


