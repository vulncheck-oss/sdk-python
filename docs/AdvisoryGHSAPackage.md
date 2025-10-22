# AdvisoryGHSAPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ecosystem** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ghsa_package import AdvisoryGHSAPackage

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGHSAPackage from a JSON string
advisory_ghsa_package_instance = AdvisoryGHSAPackage.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGHSAPackage.to_json())

# convert the object into a dict
advisory_ghsa_package_dict = advisory_ghsa_package_instance.to_dict()
# create an instance of AdvisoryGHSAPackage from a dict
advisory_ghsa_package_from_dict = AdvisoryGHSAPackage.from_dict(advisory_ghsa_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


