# AdvisoryMitreAttackRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_added** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_mitre_attack_ref import AdvisoryMitreAttackRef

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMitreAttackRef from a JSON string
advisory_mitre_attack_ref_instance = AdvisoryMitreAttackRef.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMitreAttackRef.to_json())

# convert the object into a dict
advisory_mitre_attack_ref_dict = advisory_mitre_attack_ref_instance.to_dict()
# create an instance of AdvisoryMitreAttackRef from a dict
advisory_mitre_attack_ref_from_dict = AdvisoryMitreAttackRef.from_dict(advisory_mitre_attack_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


