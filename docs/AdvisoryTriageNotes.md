# AdvisoryTriageNotes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**references** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_triage_notes import AdvisoryTriageNotes

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryTriageNotes from a JSON string
advisory_triage_notes_instance = AdvisoryTriageNotes.from_json(json)
# print the JSON string representation of the object
print(AdvisoryTriageNotes.to_json())

# convert the object into a dict
advisory_triage_notes_dict = advisory_triage_notes_instance.to_dict()
# create an instance of AdvisoryTriageNotes from a dict
advisory_triage_notes_from_dict = AdvisoryTriageNotes.from_dict(advisory_triage_notes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


