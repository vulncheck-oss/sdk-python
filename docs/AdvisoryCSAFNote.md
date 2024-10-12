# AdvisoryCSAFNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_csaf_note import AdvisoryCSAFNote

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCSAFNote from a JSON string
advisory_csaf_note_instance = AdvisoryCSAFNote.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCSAFNote.to_json())

# convert the object into a dict
advisory_csaf_note_dict = advisory_csaf_note_instance.to_dict()
# create an instance of AdvisoryCSAFNote from a dict
advisory_csaf_note_from_dict = AdvisoryCSAFNote.from_dict(advisory_csaf_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


