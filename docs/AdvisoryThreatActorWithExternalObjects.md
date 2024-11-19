# AdvisoryThreatActorWithExternalObjects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve_references** | [**List[AdvisoryCVEReference]**](AdvisoryCVEReference.md) |  | [optional] 
**date_added** | **str** |  | [optional] 
**malpedia_url** | **str** |  | [optional] 
**misp_id** | **str** |  | [optional] 
**misp_threat_actor** | [**AdvisoryMISPValueNoID**](AdvisoryMISPValueNoID.md) |  | [optional] 
**mitre_attack_group** | [**AdvisoryMITREAttackGroupNoID**](AdvisoryMITREAttackGroupNoID.md) |  | [optional] 
**mitre_id** | **str** |  | [optional] 
**threat_actor_name** | **str** |  | [optional] 
**tools** | [**List[AdvisoryTool]**](AdvisoryTool.md) |  | [optional] 
**vendor_names_for_threat_actors** | [**List[AdvisoryVendorNameForThreatActor]**](AdvisoryVendorNameForThreatActor.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_threat_actor_with_external_objects import AdvisoryThreatActorWithExternalObjects

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryThreatActorWithExternalObjects from a JSON string
advisory_threat_actor_with_external_objects_instance = AdvisoryThreatActorWithExternalObjects.from_json(json)
# print the JSON string representation of the object
print(AdvisoryThreatActorWithExternalObjects.to_json())

# convert the object into a dict
advisory_threat_actor_with_external_objects_dict = advisory_threat_actor_with_external_objects_instance.to_dict()
# create an instance of AdvisoryThreatActorWithExternalObjects from a dict
advisory_threat_actor_with_external_objects_from_dict = AdvisoryThreatActorWithExternalObjects.from_dict(advisory_threat_actor_with_external_objects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


