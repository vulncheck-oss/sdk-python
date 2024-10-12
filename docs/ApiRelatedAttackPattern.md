# ApiRelatedAttackPattern


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capec_id** | **str** |  | [optional] 
**capec_name** | **str** |  | [optional] 
**capec_url** | **str** |  | [optional] 
**lang** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_related_attack_pattern import ApiRelatedAttackPattern

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRelatedAttackPattern from a JSON string
api_related_attack_pattern_instance = ApiRelatedAttackPattern.from_json(json)
# print the JSON string representation of the object
print(ApiRelatedAttackPattern.to_json())

# convert the object into a dict
api_related_attack_pattern_dict = api_related_attack_pattern_instance.to_dict()
# create an instance of ApiRelatedAttackPattern from a dict
api_related_attack_pattern_from_dict = ApiRelatedAttackPattern.from_dict(api_related_attack_pattern_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


