# AdvisoryPyPARange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[AdvisoryPyPAEvent]**](AdvisoryPyPAEvent.md) |  | [optional] 
**ranges_type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_py_pa_range import AdvisoryPyPARange

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPyPARange from a JSON string
advisory_py_pa_range_instance = AdvisoryPyPARange.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPyPARange.to_json())

# convert the object into a dict
advisory_py_pa_range_dict = advisory_py_pa_range_instance.to_dict()
# create an instance of AdvisoryPyPARange from a dict
advisory_py_pa_range_from_dict = AdvisoryPyPARange.from_dict(advisory_py_pa_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


