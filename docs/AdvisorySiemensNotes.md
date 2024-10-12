# AdvisorySiemensNotes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_siemens_notes import AdvisorySiemensNotes

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySiemensNotes from a JSON string
advisory_siemens_notes_instance = AdvisorySiemensNotes.from_json(json)
# print the JSON string representation of the object
print(AdvisorySiemensNotes.to_json())

# convert the object into a dict
advisory_siemens_notes_dict = advisory_siemens_notes_instance.to_dict()
# create an instance of AdvisorySiemensNotes from a dict
advisory_siemens_notes_from_dict = AdvisorySiemensNotes.from_dict(advisory_siemens_notes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


