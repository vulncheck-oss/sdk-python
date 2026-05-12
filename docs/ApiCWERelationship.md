# ApiCWERelationship

api.CWERelationship

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cwe_id** | **str** |  | [optional] 
**cwe_label** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_cwe_relationship import ApiCWERelationship

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCWERelationship from a JSON string
api_cwe_relationship_instance = ApiCWERelationship.from_json(json)
# print the JSON string representation of the object
print(ApiCWERelationship.to_json())

# convert the object into a dict
api_cwe_relationship_dict = api_cwe_relationship_instance.to_dict()
# create an instance of ApiCWERelationship from a dict
api_cwe_relationship_from_dict = ApiCWERelationship.from_dict(api_cwe_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


