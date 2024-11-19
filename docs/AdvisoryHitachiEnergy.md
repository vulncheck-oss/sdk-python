# AdvisoryHitachiEnergy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory_id** | **str** |  | [optional] 
**csaf_url** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**exploited** | **bool** |  | [optional] 
**products** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_hitachi_energy import AdvisoryHitachiEnergy

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryHitachiEnergy from a JSON string
advisory_hitachi_energy_instance = AdvisoryHitachiEnergy.from_json(json)
# print the JSON string representation of the object
print(AdvisoryHitachiEnergy.to_json())

# convert the object into a dict
advisory_hitachi_energy_dict = advisory_hitachi_energy_instance.to_dict()
# create an instance of AdvisoryHitachiEnergy from a dict
advisory_hitachi_energy_from_dict = AdvisoryHitachiEnergy.from_dict(advisory_hitachi_energy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


