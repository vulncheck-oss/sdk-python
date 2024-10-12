# AdvisoryBugzilla


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_bugzilla import AdvisoryBugzilla

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBugzilla from a JSON string
advisory_bugzilla_instance = AdvisoryBugzilla.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBugzilla.to_json())

# convert the object into a dict
advisory_bugzilla_dict = advisory_bugzilla_instance.to_dict()
# create an instance of AdvisoryBugzilla from a dict
advisory_bugzilla_from_dict = AdvisoryBugzilla.from_dict(advisory_bugzilla_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


