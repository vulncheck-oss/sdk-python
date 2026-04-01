# AdvisoryGenericEOLReference

advisory.GenericEOLReference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_generic_eol_reference import AdvisoryGenericEOLReference

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGenericEOLReference from a JSON string
advisory_generic_eol_reference_instance = AdvisoryGenericEOLReference.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGenericEOLReference.to_json())

# convert the object into a dict
advisory_generic_eol_reference_dict = advisory_generic_eol_reference_instance.to_dict()
# create an instance of AdvisoryGenericEOLReference from a dict
advisory_generic_eol_reference_from_dict = AdvisoryGenericEOLReference.from_dict(advisory_generic_eol_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


