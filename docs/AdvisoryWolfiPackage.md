# AdvisoryWolfiPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**secfixes** | [**List[AdvisoryWolfiSecFix]**](AdvisoryWolfiSecFix.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_wolfi_package import AdvisoryWolfiPackage

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryWolfiPackage from a JSON string
advisory_wolfi_package_instance = AdvisoryWolfiPackage.from_json(json)
# print the JSON string representation of the object
print(AdvisoryWolfiPackage.to_json())

# convert the object into a dict
advisory_wolfi_package_dict = advisory_wolfi_package_instance.to_dict()
# create an instance of AdvisoryWolfiPackage from a dict
advisory_wolfi_package_from_dict = AdvisoryWolfiPackage.from_dict(advisory_wolfi_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


