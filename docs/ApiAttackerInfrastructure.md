# ApiAttackerInfrastructure

api.AttackerInfrastructure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_name** | **str** |  | [optional] 
**asn** | **str** |  | [optional] 
**classifications** | **List[str]** |  | [optional] 
**country** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**first_seen** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**last_seen** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**source** | **List[str]** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_attacker_infrastructure import ApiAttackerInfrastructure

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAttackerInfrastructure from a JSON string
api_attacker_infrastructure_instance = ApiAttackerInfrastructure.from_json(json)
# print the JSON string representation of the object
print(ApiAttackerInfrastructure.to_json())

# convert the object into a dict
api_attacker_infrastructure_dict = api_attacker_infrastructure_instance.to_dict()
# create an instance of ApiAttackerInfrastructure from a dict
api_attacker_infrastructure_from_dict = ApiAttackerInfrastructure.from_dict(api_attacker_infrastructure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


