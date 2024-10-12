# AdvisoryCentosPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_centos_package import AdvisoryCentosPackage

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCentosPackage from a JSON string
advisory_centos_package_instance = AdvisoryCentosPackage.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCentosPackage.to_json())

# convert the object into a dict
advisory_centos_package_dict = advisory_centos_package_instance.to_dict()
# create an instance of AdvisoryCentosPackage from a dict
advisory_centos_package_from_dict = AdvisoryCentosPackage.from_dict(advisory_centos_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


