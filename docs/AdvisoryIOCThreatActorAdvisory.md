# AdvisoryIOCThreatActorAdvisory

advisory.IOCThreatActorAdvisory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**malicious_domains** | **List[str]** |  | [optional] 
**malicious_files** | [**List[AdvisoryIOCFile]**](AdvisoryIOCFile.md) |  | [optional] 
**malicious_ip** | **List[str]** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**threat_actor_name** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ioc_threat_actor_advisory import AdvisoryIOCThreatActorAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryIOCThreatActorAdvisory from a JSON string
advisory_ioc_threat_actor_advisory_instance = AdvisoryIOCThreatActorAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryIOCThreatActorAdvisory.to_json())

# convert the object into a dict
advisory_ioc_threat_actor_advisory_dict = advisory_ioc_threat_actor_advisory_instance.to_dict()
# create an instance of AdvisoryIOCThreatActorAdvisory from a dict
advisory_ioc_threat_actor_advisory_from_dict = AdvisoryIOCThreatActorAdvisory.from_dict(advisory_ioc_threat_actor_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


