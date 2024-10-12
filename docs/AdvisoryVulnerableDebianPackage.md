# AdvisoryVulnerableDebianPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_cves** | [**List[AdvisoryDebianCVE]**](AdvisoryDebianCVE.md) |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**package_name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_vulnerable_debian_package import AdvisoryVulnerableDebianPackage

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVulnerableDebianPackage from a JSON string
advisory_vulnerable_debian_package_instance = AdvisoryVulnerableDebianPackage.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVulnerableDebianPackage.to_json())

# convert the object into a dict
advisory_vulnerable_debian_package_dict = advisory_vulnerable_debian_package_instance.to_dict()
# create an instance of AdvisoryVulnerableDebianPackage from a dict
advisory_vulnerable_debian_package_from_dict = AdvisoryVulnerableDebianPackage.from_dict(advisory_vulnerable_debian_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


