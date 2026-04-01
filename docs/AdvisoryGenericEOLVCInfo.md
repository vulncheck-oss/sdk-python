# AdvisoryGenericEOLVCInfo

advisory.GenericEOLVCInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | [**List[AdvisoryGenericEOLReference]**](AdvisoryGenericEOLReference.md) |  | [optional] 
**replacement** | [**AdvisoryGenericEOLProduct**](AdvisoryGenericEOLProduct.md) |  | [optional] 
**updated_at** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_generic_eolvc_info import AdvisoryGenericEOLVCInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGenericEOLVCInfo from a JSON string
advisory_generic_eolvc_info_instance = AdvisoryGenericEOLVCInfo.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGenericEOLVCInfo.to_json())

# convert the object into a dict
advisory_generic_eolvc_info_dict = advisory_generic_eolvc_info_instance.to_dict()
# create an instance of AdvisoryGenericEOLVCInfo from a dict
advisory_generic_eolvc_info_from_dict = AdvisoryGenericEOLVCInfo.from_dict(advisory_generic_eolvc_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


