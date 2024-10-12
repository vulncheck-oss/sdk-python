# AdvisoryAdvisoryRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**external_id** | **List[str]** |  | [optional] 
**lang** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**refsource** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_advisory_record import AdvisoryAdvisoryRecord

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAdvisoryRecord from a JSON string
advisory_advisory_record_instance = AdvisoryAdvisoryRecord.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAdvisoryRecord.to_json())

# convert the object into a dict
advisory_advisory_record_dict = advisory_advisory_record_instance.to_dict()
# create an instance of AdvisoryAdvisoryRecord from a dict
advisory_advisory_record_from_dict = AdvisoryAdvisoryRecord.from_dict(advisory_advisory_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


