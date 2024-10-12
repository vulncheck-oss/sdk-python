# AdvisoryAlpineLinuxSecurityFix


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **str** |  | [optional] 
**fixed_version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_alpine_linux_security_fix import AdvisoryAlpineLinuxSecurityFix

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAlpineLinuxSecurityFix from a JSON string
advisory_alpine_linux_security_fix_instance = AdvisoryAlpineLinuxSecurityFix.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAlpineLinuxSecurityFix.to_json())

# convert the object into a dict
advisory_alpine_linux_security_fix_dict = advisory_alpine_linux_security_fix_instance.to_dict()
# create an instance of AdvisoryAlpineLinuxSecurityFix from a dict
advisory_alpine_linux_security_fix_from_dict = AdvisoryAlpineLinuxSecurityFix.from_dict(advisory_alpine_linux_security_fix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


