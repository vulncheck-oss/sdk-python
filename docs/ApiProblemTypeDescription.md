# ApiProblemTypeDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lang** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_problem_type_description import ApiProblemTypeDescription

# TODO update the JSON string below
json = "{}"
# create an instance of ApiProblemTypeDescription from a JSON string
api_problem_type_description_instance = ApiProblemTypeDescription.from_json(json)
# print the JSON string representation of the object
print(ApiProblemTypeDescription.to_json())

# convert the object into a dict
api_problem_type_description_dict = api_problem_type_description_instance.to_dict()
# create an instance of ApiProblemTypeDescription from a dict
api_problem_type_description_from_dict = ApiProblemTypeDescription.from_dict(api_problem_type_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


