# ApiProblemTypeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**List[ApiProblemTypeDescription]**](ApiProblemTypeDescription.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_problem_type_data import ApiProblemTypeData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiProblemTypeData from a JSON string
api_problem_type_data_instance = ApiProblemTypeData.from_json(json)
# print the JSON string representation of the object
print(ApiProblemTypeData.to_json())

# convert the object into a dict
api_problem_type_data_dict = api_problem_type_data_instance.to_dict()
# create an instance of ApiProblemTypeData from a dict
api_problem_type_data_from_dict = ApiProblemTypeData.from_dict(api_problem_type_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


