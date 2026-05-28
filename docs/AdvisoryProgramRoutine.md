# AdvisoryProgramRoutine

advisory.ProgramRoutine

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_program_routine import AdvisoryProgramRoutine

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryProgramRoutine from a JSON string
advisory_program_routine_instance = AdvisoryProgramRoutine.from_json(json)
# print the JSON string representation of the object
print(AdvisoryProgramRoutine.to_json())

# convert the object into a dict
advisory_program_routine_dict = advisory_program_routine_instance.to_dict()
# create an instance of AdvisoryProgramRoutine from a dict
advisory_program_routine_from_dict = AdvisoryProgramRoutine.from_dict(advisory_program_routine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


