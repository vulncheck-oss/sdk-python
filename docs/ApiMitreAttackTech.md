# ApiMitreAttackTech


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**d3fendmapping** | [**List[ApiMitreMitigation2D3fendMapping]**](ApiMitreMitigation2D3fendMapping.md) |  | [optional] 
**detections** | [**List[ApiMitreDetectionTech]**](ApiMitreDetectionTech.md) |  | [optional] 
**domain** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**mitigations** | [**List[ApiMitreMitigationTech]**](ApiMitreMitigationTech.md) |  | [optional] 
**name** | **str** |  | [optional] 
**subtechnique** | **bool** |  | [optional] 
**tactics** | **List[str]** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_mitre_attack_tech import ApiMitreAttackTech

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMitreAttackTech from a JSON string
api_mitre_attack_tech_instance = ApiMitreAttackTech.from_json(json)
# print the JSON string representation of the object
print(ApiMitreAttackTech.to_json())

# convert the object into a dict
api_mitre_attack_tech_dict = api_mitre_attack_tech_instance.to_dict()
# create an instance of ApiMitreAttackTech from a dict
api_mitre_attack_tech_from_dict = ApiMitreAttackTech.from_dict(api_mitre_attack_tech_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


