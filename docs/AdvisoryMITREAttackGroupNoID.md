# AdvisoryMITREAttackGroupNoID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**techniques** | [**List[AdvisoryMitreAttackTechnique]**](AdvisoryMitreAttackTechnique.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_mitre_attack_group_no_id import AdvisoryMITREAttackGroupNoID

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMITREAttackGroupNoID from a JSON string
advisory_mitre_attack_group_no_id_instance = AdvisoryMITREAttackGroupNoID.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMITREAttackGroupNoID.to_json())

# convert the object into a dict
advisory_mitre_attack_group_no_id_dict = advisory_mitre_attack_group_no_id_instance.to_dict()
# create an instance of AdvisoryMITREAttackGroupNoID from a dict
advisory_mitre_attack_group_no_id_from_dict = AdvisoryMITREAttackGroupNoID.from_dict(advisory_mitre_attack_group_no_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


