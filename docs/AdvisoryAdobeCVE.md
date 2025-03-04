# AdvisoryAdobeCVE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **str** |  | [optional] 
**cvss_score** | **str** |  | [optional] 
**cvss_vector** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_adobe_cve import AdvisoryAdobeCVE

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAdobeCVE from a JSON string
advisory_adobe_cve_instance = AdvisoryAdobeCVE.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAdobeCVE.to_json())

# convert the object into a dict
advisory_adobe_cve_dict = advisory_adobe_cve_instance.to_dict()
# create an instance of AdvisoryAdobeCVE from a dict
advisory_adobe_cve_from_dict = AdvisoryAdobeCVE.from_dict(advisory_adobe_cve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


