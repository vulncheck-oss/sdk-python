# AdvisoryMitreAttackTechnique


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_technique** | **str** |  | [optional] 
**sub_technique_name** | **str** |  | [optional] 
**tactic** | **List[str]** |  | [optional] 
**technique_id** | **str** |  | [optional] 
**technique_name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_mitre_attack_technique import AdvisoryMitreAttackTechnique

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMitreAttackTechnique from a JSON string
advisory_mitre_attack_technique_instance = AdvisoryMitreAttackTechnique.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMitreAttackTechnique.to_json())

# convert the object into a dict
advisory_mitre_attack_technique_dict = advisory_mitre_attack_technique_instance.to_dict()
# create an instance of AdvisoryMitreAttackTechnique from a dict
advisory_mitre_attack_technique_from_dict = AdvisoryMitreAttackTechnique.from_dict(advisory_mitre_attack_technique_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


