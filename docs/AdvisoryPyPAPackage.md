# AdvisoryPyPAPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ecosystem** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**purl** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_py_pa_package import AdvisoryPyPAPackage

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPyPAPackage from a JSON string
advisory_py_pa_package_instance = AdvisoryPyPAPackage.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPyPAPackage.to_json())

# convert the object into a dict
advisory_py_pa_package_dict = advisory_py_pa_package_instance.to_dict()
# create an instance of AdvisoryPyPAPackage from a dict
advisory_py_pa_package_from_dict = AdvisoryPyPAPackage.from_dict(advisory_py_pa_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


