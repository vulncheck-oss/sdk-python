# AdvisoryAffectedDebianPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_affected_debian_package import AdvisoryAffectedDebianPackage

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAffectedDebianPackage from a JSON string
advisory_affected_debian_package_instance = AdvisoryAffectedDebianPackage.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAffectedDebianPackage.to_json())

# convert the object into a dict
advisory_affected_debian_package_dict = advisory_affected_debian_package_instance.to_dict()
# create an instance of AdvisoryAffectedDebianPackage from a dict
advisory_affected_debian_package_from_dict = AdvisoryAffectedDebianPackage.from_dict(advisory_affected_debian_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


