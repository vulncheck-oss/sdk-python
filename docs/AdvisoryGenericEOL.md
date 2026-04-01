# AdvisoryGenericEOL

advisory.GenericEOL

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**core** | [**AdvisoryGenericEOLCore**](AdvisoryGenericEOLCore.md) |  | [optional] 
**product** | [**AdvisoryGenericEOLProduct**](AdvisoryGenericEOLProduct.md) |  | [optional] 
**vc_info** | [**AdvisoryGenericEOLVCInfo**](AdvisoryGenericEOLVCInfo.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_generic_eol import AdvisoryGenericEOL

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGenericEOL from a JSON string
advisory_generic_eol_instance = AdvisoryGenericEOL.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGenericEOL.to_json())

# convert the object into a dict
advisory_generic_eol_dict = advisory_generic_eol_instance.to_dict()
# create an instance of AdvisoryGenericEOL from a dict
advisory_generic_eol_from_dict = AdvisoryGenericEOL.from_dict(advisory_generic_eol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


