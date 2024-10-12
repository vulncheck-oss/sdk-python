# AdvisoryJVNReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_jvn_reference import AdvisoryJVNReference

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryJVNReference from a JSON string
advisory_jvn_reference_instance = AdvisoryJVNReference.from_json(json)
# print the JSON string representation of the object
print(AdvisoryJVNReference.to_json())

# convert the object into a dict
advisory_jvn_reference_dict = advisory_jvn_reference_instance.to_dict()
# create an instance of AdvisoryJVNReference from a dict
advisory_jvn_reference_from_dict = AdvisoryJVNReference.from_dict(advisory_jvn_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


