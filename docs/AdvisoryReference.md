# AdvisoryReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | sort | [optional] 
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_reference import AdvisoryReference

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryReference from a JSON string
advisory_reference_instance = AdvisoryReference.from_json(json)
# print the JSON string representation of the object
print(AdvisoryReference.to_json())

# convert the object into a dict
advisory_reference_dict = advisory_reference_instance.to_dict()
# create an instance of AdvisoryReference from a dict
advisory_reference_from_dict = AdvisoryReference.from_dict(advisory_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


