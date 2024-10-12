# AdvisoryIpIntelRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**feed_ids** | **List[str]** |  | [optional] 
**hostnames** | **List[str]** |  | [optional] 
**ip** | **str** |  | [optional] 
**last_seen** | **str** |  | [optional] 
**matches** | **List[str]** |  | [optional] 
**port** | **int** |  | [optional] 
**ssl** | **bool** |  | [optional] 
**type** | [**AdvisoryRecordType**](AdvisoryRecordType.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ip_intel_record import AdvisoryIpIntelRecord

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryIpIntelRecord from a JSON string
advisory_ip_intel_record_instance = AdvisoryIpIntelRecord.from_json(json)
# print the JSON string representation of the object
print(AdvisoryIpIntelRecord.to_json())

# convert the object into a dict
advisory_ip_intel_record_dict = advisory_ip_intel_record_instance.to_dict()
# create an instance of AdvisoryIpIntelRecord from a dict
advisory_ip_intel_record_from_dict = AdvisoryIpIntelRecord.from_dict(advisory_ip_intel_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


