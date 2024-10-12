# AdvisoryAlmaReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_alma_reference import AdvisoryAlmaReference

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAlmaReference from a JSON string
advisory_alma_reference_instance = AdvisoryAlmaReference.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAlmaReference.to_json())

# convert the object into a dict
advisory_alma_reference_dict = advisory_alma_reference_instance.to_dict()
# create an instance of AdvisoryAlmaReference from a dict
advisory_alma_reference_from_dict = AdvisoryAlmaReference.from_dict(advisory_alma_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


