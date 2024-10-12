# AdvisoryPyPAAdvisoryAffectedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package** | [**AdvisoryPyPAAdvisoryAffectedInnerPackage**](AdvisoryPyPAAdvisoryAffectedInnerPackage.md) |  | [optional] 
**ranges** | [**List[AdvisoryPyPAAdvisoryAffectedInnerRangesInner]**](AdvisoryPyPAAdvisoryAffectedInnerRangesInner.md) |  | [optional] 
**versions** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_py_pa_advisory_affected_inner import AdvisoryPyPAAdvisoryAffectedInner

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPyPAAdvisoryAffectedInner from a JSON string
advisory_py_pa_advisory_affected_inner_instance = AdvisoryPyPAAdvisoryAffectedInner.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPyPAAdvisoryAffectedInner.to_json())

# convert the object into a dict
advisory_py_pa_advisory_affected_inner_dict = advisory_py_pa_advisory_affected_inner_instance.to_dict()
# create an instance of AdvisoryPyPAAdvisoryAffectedInner from a dict
advisory_py_pa_advisory_affected_inner_from_dict = AdvisoryPyPAAdvisoryAffectedInner.from_dict(advisory_py_pa_advisory_affected_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


