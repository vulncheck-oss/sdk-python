# AdvisorySchneiderCVE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **str** |  | [optional] 
**cvss_score3** | **str** |  | [optional] 
**cvss_score4** | **str** |  | [optional] 
**cvss_vector3** | **str** |  | [optional] 
**cvss_vector4** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_schneider_cve import AdvisorySchneiderCVE

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySchneiderCVE from a JSON string
advisory_schneider_cve_instance = AdvisorySchneiderCVE.from_json(json)
# print the JSON string representation of the object
print(AdvisorySchneiderCVE.to_json())

# convert the object into a dict
advisory_schneider_cve_dict = advisory_schneider_cve_instance.to_dict()
# create an instance of AdvisorySchneiderCVE from a dict
advisory_schneider_cve_from_dict = AdvisorySchneiderCVE.from_dict(advisory_schneider_cve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


