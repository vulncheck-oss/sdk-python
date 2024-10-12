# ApiProblemTypeExtended


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**problemtype_data** | [**List[ApiProblemTypeDataExtended]**](ApiProblemTypeDataExtended.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_problem_type_extended import ApiProblemTypeExtended

# TODO update the JSON string below
json = "{}"
# create an instance of ApiProblemTypeExtended from a JSON string
api_problem_type_extended_instance = ApiProblemTypeExtended.from_json(json)
# print the JSON string representation of the object
print(ApiProblemTypeExtended.to_json())

# convert the object into a dict
api_problem_type_extended_dict = api_problem_type_extended_instance.to_dict()
# create an instance of ApiProblemTypeExtended from a dict
api_problem_type_extended_from_dict = ApiProblemTypeExtended.from_dict(api_problem_type_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


