# AdvisoryOverrideAnnotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve_id** | **str** |  | [optional] 
**modified** | **str** |  | [optional] 
**published** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**snapshot** | **str** |  | [optional] 
**triage_notes** | [**AdvisoryTriageNotes**](AdvisoryTriageNotes.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_override_annotation import AdvisoryOverrideAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOverrideAnnotation from a JSON string
advisory_override_annotation_instance = AdvisoryOverrideAnnotation.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOverrideAnnotation.to_json())

# convert the object into a dict
advisory_override_annotation_dict = advisory_override_annotation_instance.to_dict()
# create an instance of AdvisoryOverrideAnnotation from a dict
advisory_override_annotation_from_dict = AdvisoryOverrideAnnotation.from_dict(advisory_override_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


