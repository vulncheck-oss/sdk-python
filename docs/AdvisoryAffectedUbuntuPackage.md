# AdvisoryAffectedUbuntuPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**break_commit_url** | **List[str]** |  | [optional] 
**fix_commit_url** | **List[str]** |  | [optional] 
**package_name** | **str** |  | [optional] 
**package_release_status** | [**List[AdvisoryUbuntuPackageReleaseStatus]**](AdvisoryUbuntuPackageReleaseStatus.md) |  | [optional] 
**upstream_fix_url** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_affected_ubuntu_package import AdvisoryAffectedUbuntuPackage

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAffectedUbuntuPackage from a JSON string
advisory_affected_ubuntu_package_instance = AdvisoryAffectedUbuntuPackage.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAffectedUbuntuPackage.to_json())

# convert the object into a dict
advisory_affected_ubuntu_package_dict = advisory_affected_ubuntu_package_instance.to_dict()
# create an instance of AdvisoryAffectedUbuntuPackage from a dict
advisory_affected_ubuntu_package_from_dict = AdvisoryAffectedUbuntuPackage.from_dict(advisory_affected_ubuntu_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


