# AdvisoryVCVulnerableCPEs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **str** |  | [optional] 
**unrolled** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_vc_vulnerable_cpes import AdvisoryVCVulnerableCPEs

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVCVulnerableCPEs from a JSON string
advisory_vc_vulnerable_cpes_instance = AdvisoryVCVulnerableCPEs.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVCVulnerableCPEs.to_json())

# convert the object into a dict
advisory_vc_vulnerable_cpes_dict = advisory_vc_vulnerable_cpes_instance.to_dict()
# create an instance of AdvisoryVCVulnerableCPEs from a dict
advisory_vc_vulnerable_cpes_from_dict = AdvisoryVCVulnerableCPEs.from_dict(advisory_vc_vulnerable_cpes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


