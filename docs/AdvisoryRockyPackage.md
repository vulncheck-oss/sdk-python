# AdvisoryRockyPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distro** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_rocky_package import AdvisoryRockyPackage

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRockyPackage from a JSON string
advisory_rocky_package_instance = AdvisoryRockyPackage.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRockyPackage.to_json())

# convert the object into a dict
advisory_rocky_package_dict = advisory_rocky_package_instance.to_dict()
# create an instance of AdvisoryRockyPackage from a dict
advisory_rocky_package_from_dict = AdvisoryRockyPackage.from_dict(advisory_rocky_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


