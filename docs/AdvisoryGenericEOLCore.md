# AdvisoryGenericEOLCore

advisory.GenericEOLCore

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_of_life** | **str** |  | [optional] 
**end_of_sales** | **str** |  | [optional] 
**end_of_security_support** | **str** |  | [optional] 
**last_updated** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_generic_eol_core import AdvisoryGenericEOLCore

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGenericEOLCore from a JSON string
advisory_generic_eol_core_instance = AdvisoryGenericEOLCore.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGenericEOLCore.to_json())

# convert the object into a dict
advisory_generic_eol_core_dict = advisory_generic_eol_core_instance.to_dict()
# create an instance of AdvisoryGenericEOLCore from a dict
advisory_generic_eol_core_from_dict = AdvisoryGenericEOLCore.from_dict(advisory_generic_eol_core_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


