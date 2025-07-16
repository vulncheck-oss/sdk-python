# AdvisoryMitreAttackTechWithRefs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**references** | [**List[AdvisoryMitreAttackRef]**](AdvisoryMitreAttackRef.md) |  | [optional] 
**subtechnique** | **bool** |  | [optional] 
**tactics** | **List[str]** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_mitre_attack_tech_with_refs import AdvisoryMitreAttackTechWithRefs

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMitreAttackTechWithRefs from a JSON string
advisory_mitre_attack_tech_with_refs_instance = AdvisoryMitreAttackTechWithRefs.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMitreAttackTechWithRefs.to_json())

# convert the object into a dict
advisory_mitre_attack_tech_with_refs_dict = advisory_mitre_attack_tech_with_refs_instance.to_dict()
# create an instance of AdvisoryMitreAttackTechWithRefs from a dict
advisory_mitre_attack_tech_with_refs_from_dict = AdvisoryMitreAttackTechWithRefs.from_dict(advisory_mitre_attack_tech_with_refs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


