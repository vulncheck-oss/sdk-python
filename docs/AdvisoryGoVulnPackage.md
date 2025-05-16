# AdvisoryGoVulnPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ecosystem** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_go_vuln_package import AdvisoryGoVulnPackage

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGoVulnPackage from a JSON string
advisory_go_vuln_package_instance = AdvisoryGoVulnPackage.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGoVulnPackage.to_json())

# convert the object into a dict
advisory_go_vuln_package_dict = advisory_go_vuln_package_instance.to_dict()
# create an instance of AdvisoryGoVulnPackage from a dict
advisory_go_vuln_package_from_dict = AdvisoryGoVulnPackage.from_dict(advisory_go_vuln_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


