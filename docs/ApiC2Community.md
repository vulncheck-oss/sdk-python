# ApiC2Community

api.C2Community

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
from vulncheck_sdk.models.api_c2_community import ApiC2Community

# TODO update the JSON string below
json = "{}"
# create an instance of ApiC2Community from a JSON string
api_c2_community_instance = ApiC2Community.from_json(json)
# print the JSON string representation of the object
print(ApiC2Community.to_json())

# convert the object into a dict
api_c2_community_dict = api_c2_community_instance.to_dict()
# create an instance of ApiC2Community from a dict
api_c2_community_from_dict = ApiC2Community.from_dict(api_c2_community_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


