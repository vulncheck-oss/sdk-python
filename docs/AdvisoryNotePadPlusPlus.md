# AdvisoryNotePadPlusPlus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_note_pad_plus_plus import AdvisoryNotePadPlusPlus

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNotePadPlusPlus from a JSON string
advisory_note_pad_plus_plus_instance = AdvisoryNotePadPlusPlus.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNotePadPlusPlus.to_json())

# convert the object into a dict
advisory_note_pad_plus_plus_dict = advisory_note_pad_plus_plus_instance.to_dict()
# create an instance of AdvisoryNotePadPlusPlus from a dict
advisory_note_pad_plus_plus_from_dict = AdvisoryNotePadPlusPlus.from_dict(advisory_note_pad_plus_plus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


