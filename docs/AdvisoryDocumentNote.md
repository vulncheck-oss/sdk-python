# AdvisoryDocumentNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_document_note import AdvisoryDocumentNote

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryDocumentNote from a JSON string
advisory_document_note_instance = AdvisoryDocumentNote.from_json(json)
# print the JSON string representation of the object
print(AdvisoryDocumentNote.to_json())

# convert the object into a dict
advisory_document_note_dict = advisory_document_note_instance.to_dict()
# create an instance of AdvisoryDocumentNote from a dict
advisory_document_note_from_dict = AdvisoryDocumentNote.from_dict(advisory_document_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


