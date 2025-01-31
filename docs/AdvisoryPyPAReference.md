# AdvisoryPyPAReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refs_type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_py_pa_reference import AdvisoryPyPAReference

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPyPAReference from a JSON string
advisory_py_pa_reference_instance = AdvisoryPyPAReference.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPyPAReference.to_json())

# convert the object into a dict
advisory_py_pa_reference_dict = advisory_py_pa_reference_instance.to_dict()
# create an instance of AdvisoryPyPAReference from a dict
advisory_py_pa_reference_from_dict = AdvisoryPyPAReference.from_dict(advisory_py_pa_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


