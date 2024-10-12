# ApiProblemTypeDescriptionExtended


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lang** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_problem_type_description_extended import ApiProblemTypeDescriptionExtended

# TODO update the JSON string below
json = "{}"
# create an instance of ApiProblemTypeDescriptionExtended from a JSON string
api_problem_type_description_extended_instance = ApiProblemTypeDescriptionExtended.from_json(json)
# print the JSON string representation of the object
print(ApiProblemTypeDescriptionExtended.to_json())

# convert the object into a dict
api_problem_type_description_extended_dict = api_problem_type_description_extended_instance.to_dict()
# create an instance of ApiProblemTypeDescriptionExtended from a dict
api_problem_type_description_extended_from_dict = ApiProblemTypeDescriptionExtended.from_dict(api_problem_type_description_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


