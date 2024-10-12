# AdvisoryRNote


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audience** | **str** |  | [optional] 
**ordinal** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **int** | diff between xml &amp;&amp; json | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_r_note import AdvisoryRNote

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRNote from a JSON string
advisory_r_note_instance = AdvisoryRNote.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRNote.to_json())

# convert the object into a dict
advisory_r_note_dict = advisory_r_note_instance.to_dict()
# create an instance of AdvisoryRNote from a dict
advisory_r_note_from_dict = AdvisoryRNote.from_dict(advisory_r_note_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


