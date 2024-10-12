# AdvisoryRecordType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finding** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_record_type import AdvisoryRecordType

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRecordType from a JSON string
advisory_record_type_instance = AdvisoryRecordType.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRecordType.to_json())

# convert the object into a dict
advisory_record_type_dict = advisory_record_type_instance.to_dict()
# create an instance of AdvisoryRecordType from a dict
advisory_record_type_from_dict = AdvisoryRecordType.from_dict(advisory_record_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


