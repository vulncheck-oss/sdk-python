# ApiMitreAttackToCVE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve_list** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**technique_id** | [**ApiMitreAttackTech**](ApiMitreAttackTech.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_mitre_attack_to_cve import ApiMitreAttackToCVE

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMitreAttackToCVE from a JSON string
api_mitre_attack_to_cve_instance = ApiMitreAttackToCVE.from_json(json)
# print the JSON string representation of the object
print(ApiMitreAttackToCVE.to_json())

# convert the object into a dict
api_mitre_attack_to_cve_dict = api_mitre_attack_to_cve_instance.to_dict()
# create an instance of ApiMitreAttackToCVE from a dict
api_mitre_attack_to_cve_from_dict = ApiMitreAttackToCVE.from_dict(api_mitre_attack_to_cve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


