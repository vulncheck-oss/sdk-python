# AdvisoryPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | [optional] 
**name** | **str** | sort | [optional] 
**release** | **str** |  | [optional] 
**src** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_package import AdvisoryPackage

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPackage from a JSON string
advisory_package_instance = AdvisoryPackage.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPackage.to_json())

# convert the object into a dict
advisory_package_dict = advisory_package_instance.to_dict()
# create an instance of AdvisoryPackage from a dict
advisory_package_from_dict = AdvisoryPackage.from_dict(advisory_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


