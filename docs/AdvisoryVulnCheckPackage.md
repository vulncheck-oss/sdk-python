# AdvisoryVulnCheckPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arch** | **str** |  | [optional] 
**distro** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**md5** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**purl** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_vuln_check_package import AdvisoryVulnCheckPackage

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVulnCheckPackage from a JSON string
advisory_vuln_check_package_instance = AdvisoryVulnCheckPackage.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVulnCheckPackage.to_json())

# convert the object into a dict
advisory_vuln_check_package_dict = advisory_vuln_check_package_instance.to_dict()
# create an instance of AdvisoryVulnCheckPackage from a dict
advisory_vuln_check_package_from_dict = AdvisoryVulnCheckPackage.from_dict(advisory_vuln_check_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


