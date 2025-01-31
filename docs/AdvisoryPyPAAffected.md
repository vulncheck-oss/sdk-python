# AdvisoryPyPAAffected


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package** | [**AdvisoryPyPAPackage**](AdvisoryPyPAPackage.md) |  | [optional] 
**ranges** | [**List[AdvisoryPyPARange]**](AdvisoryPyPARange.md) |  | [optional] 
**versions** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_py_pa_affected import AdvisoryPyPAAffected

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPyPAAffected from a JSON string
advisory_py_pa_affected_instance = AdvisoryPyPAAffected.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPyPAAffected.to_json())

# convert the object into a dict
advisory_py_pa_affected_dict = advisory_py_pa_affected_instance.to_dict()
# create an instance of AdvisoryPyPAAffected from a dict
advisory_py_pa_affected_from_dict = AdvisoryPyPAAffected.from_dict(advisory_py_pa_affected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


