# AdvisoryMProblemTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descriptions** | [**List[AdvisoryPTMDescriptions]**](AdvisoryPTMDescriptions.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_m_problem_types import AdvisoryMProblemTypes

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMProblemTypes from a JSON string
advisory_m_problem_types_instance = AdvisoryMProblemTypes.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMProblemTypes.to_json())

# convert the object into a dict
advisory_m_problem_types_dict = advisory_m_problem_types_instance.to_dict()
# create an instance of AdvisoryMProblemTypes from a dict
advisory_m_problem_types_from_dict = AdvisoryMProblemTypes.from_dict(advisory_m_problem_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


