# AdvisoryRocheCVE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **str** |  | [optional] 
**cvss_score** | **str** |  | [optional] 
**cvss_vector** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_roche_cve import AdvisoryRocheCVE

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRocheCVE from a JSON string
advisory_roche_cve_instance = AdvisoryRocheCVE.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRocheCVE.to_json())

# convert the object into a dict
advisory_roche_cve_dict = advisory_roche_cve_instance.to_dict()
# create an instance of AdvisoryRocheCVE from a dict
advisory_roche_cve_from_dict = AdvisoryRocheCVE.from_dict(advisory_roche_cve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


