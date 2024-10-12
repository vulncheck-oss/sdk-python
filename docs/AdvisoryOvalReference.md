# AdvisoryOvalReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref_id** | **str** |  | [optional] 
**ref_url** | **str** |  | [optional] 
**source** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_oval_reference import AdvisoryOvalReference

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOvalReference from a JSON string
advisory_oval_reference_instance = AdvisoryOvalReference.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOvalReference.to_json())

# convert the object into a dict
advisory_oval_reference_dict = advisory_oval_reference_instance.to_dict()
# create an instance of AdvisoryOvalReference from a dict
advisory_oval_reference_from_dict = AdvisoryOvalReference.from_dict(advisory_oval_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


