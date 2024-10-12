# AdvisoryGHPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ecosystem** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_gh_package import AdvisoryGHPackage

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGHPackage from a JSON string
advisory_gh_package_instance = AdvisoryGHPackage.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGHPackage.to_json())

# convert the object into a dict
advisory_gh_package_dict = advisory_gh_package_instance.to_dict()
# create an instance of AdvisoryGHPackage from a dict
advisory_gh_package_from_dict = AdvisoryGHPackage.from_dict(advisory_gh_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


