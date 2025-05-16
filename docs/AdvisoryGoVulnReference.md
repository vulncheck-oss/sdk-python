# AdvisoryGoVulnReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_go_vuln_reference import AdvisoryGoVulnReference

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGoVulnReference from a JSON string
advisory_go_vuln_reference_instance = AdvisoryGoVulnReference.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGoVulnReference.to_json())

# convert the object into a dict
advisory_go_vuln_reference_dict = advisory_go_vuln_reference_instance.to_dict()
# create an instance of AdvisoryGoVulnReference from a dict
advisory_go_vuln_reference_from_dict = AdvisoryGoVulnReference.from_dict(advisory_go_vuln_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


