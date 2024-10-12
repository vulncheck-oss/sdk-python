# AdvisoryRockyAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_products** | **List[str]** |  | [optional] 
**build_references** | **List[str]** |  | [optional] 
**cves** | [**List[AdvisoryRockyCve]**](AdvisoryRockyCve.md) |  | [optional] 
**description** | **str** |  | [optional] 
**fixes** | [**List[AdvisoryRockyFix]**](AdvisoryRockyFix.md) |  | [optional] 
**name** | **str** |  | [optional] 
**published_at** | **str** |  | [optional] 
**reboot_suggested** | **bool** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**rpms** | [**Dict[str, AdvisoryRockyVersion]**](AdvisoryRockyVersion.md) |  | [optional] 
**severity** | **str** |  | [optional] 
**short_code** | **str** |  | [optional] 
**solution** | **str** |  | [optional] 
**synopsis** | **str** |  | [optional] 
**topic** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_rocky_advisory import AdvisoryRockyAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRockyAdvisory from a JSON string
advisory_rocky_advisory_instance = AdvisoryRockyAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRockyAdvisory.to_json())

# convert the object into a dict
advisory_rocky_advisory_dict = advisory_rocky_advisory_instance.to_dict()
# create an instance of AdvisoryRockyAdvisory from a dict
advisory_rocky_advisory_from_dict = AdvisoryRockyAdvisory.from_dict(advisory_rocky_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


