# ApiProblemTypeDataExtended


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**List[ApiProblemTypeDescriptionExtended]**](ApiProblemTypeDescriptionExtended.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_problem_type_data_extended import ApiProblemTypeDataExtended

# TODO update the JSON string below
json = "{}"
# create an instance of ApiProblemTypeDataExtended from a JSON string
api_problem_type_data_extended_instance = ApiProblemTypeDataExtended.from_json(json)
# print the JSON string representation of the object
print(ApiProblemTypeDataExtended.to_json())

# convert the object into a dict
api_problem_type_data_extended_dict = api_problem_type_data_extended_instance.to_dict()
# create an instance of ApiProblemTypeDataExtended from a dict
api_problem_type_data_extended_from_dict = ApiProblemTypeDataExtended.from_dict(api_problem_type_data_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


