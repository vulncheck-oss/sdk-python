# AdvisoryNote

advisory.Note

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value is the note&#39;s text in MSRC&#39;s JSON CVRF, which names it Value; Text only ever held it in the XML form. | [optional] 
**ordinal** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **int** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_note import AdvisoryNote

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNote from a JSON string
advisory_note_instance = AdvisoryNote.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNote.to_json())

# convert the object into a dict
advisory_note_dict = advisory_note_instance.to_dict()
# create an instance of AdvisoryNote from a dict
advisory_note_from_dict = AdvisoryNote.from_dict(advisory_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


