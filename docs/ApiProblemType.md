# ApiProblemType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**problemtype_data** | [**List[ApiProblemTypeData]**](ApiProblemTypeData.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_problem_type import ApiProblemType

# TODO update the JSON string below
json = "{}"
# create an instance of ApiProblemType from a JSON string
api_problem_type_instance = ApiProblemType.from_json(json)
# print the JSON string representation of the object
print(ApiProblemType.to_json())

# convert the object into a dict
api_problem_type_dict = api_problem_type_instance.to_dict()
# create an instance of ApiProblemType from a dict
api_problem_type_from_dict = ApiProblemType.from_dict(api_problem_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


