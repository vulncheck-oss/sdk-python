# AdvisoryAlpineLinuxSecDBPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_name** | **str** |  | [optional] 
**secfixes** | [**List[AdvisoryAlpineLinuxSecurityFix]**](AdvisoryAlpineLinuxSecurityFix.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_alpine_linux_sec_db_package import AdvisoryAlpineLinuxSecDBPackage

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAlpineLinuxSecDBPackage from a JSON string
advisory_alpine_linux_sec_db_package_instance = AdvisoryAlpineLinuxSecDBPackage.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAlpineLinuxSecDBPackage.to_json())

# convert the object into a dict
advisory_alpine_linux_sec_db_package_dict = advisory_alpine_linux_sec_db_package_instance.to_dict()
# create an instance of AdvisoryAlpineLinuxSecDBPackage from a dict
advisory_alpine_linux_sec_db_package_from_dict = AdvisoryAlpineLinuxSecDBPackage.from_dict(advisory_alpine_linux_sec_db_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


