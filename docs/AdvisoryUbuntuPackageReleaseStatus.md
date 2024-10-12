# AdvisoryUbuntuPackageReleaseStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **bool** |  | [optional] 
**fixed** | **bool** |  | [optional] 
**fixed_version** | **str** |  | [optional] 
**lts** | **bool** |  | [optional] 
**release** | **str** |  | [optional] 
**release_long** | **str** |  | [optional] 
**release_version** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ubuntu_package_release_status import AdvisoryUbuntuPackageReleaseStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryUbuntuPackageReleaseStatus from a JSON string
advisory_ubuntu_package_release_status_instance = AdvisoryUbuntuPackageReleaseStatus.from_json(json)
# print the JSON string representation of the object
print(AdvisoryUbuntuPackageReleaseStatus.to_json())

# convert the object into a dict
advisory_ubuntu_package_release_status_dict = advisory_ubuntu_package_release_status_instance.to_dict()
# create an instance of AdvisoryUbuntuPackageReleaseStatus from a dict
advisory_ubuntu_package_release_status_from_dict = AdvisoryUbuntuPackageReleaseStatus.from_dict(advisory_ubuntu_package_release_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


