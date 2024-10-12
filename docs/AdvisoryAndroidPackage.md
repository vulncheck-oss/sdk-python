# AdvisoryAndroidPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ecosystem** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_android_package import AdvisoryAndroidPackage

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAndroidPackage from a JSON string
advisory_android_package_instance = AdvisoryAndroidPackage.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAndroidPackage.to_json())

# convert the object into a dict
advisory_android_package_dict = advisory_android_package_instance.to_dict()
# create an instance of AdvisoryAndroidPackage from a dict
advisory_android_package_from_dict = AdvisoryAndroidPackage.from_dict(advisory_android_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


