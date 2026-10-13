# NvdsourceNvdSource

nvdsource.NvdSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_email** | **str** |  | [optional] 
**created** | **str** |  | [optional] 
**cwe_acceptance_level** | [**NvdsourceNvdAcceptanceLevel**](NvdsourceNvdAcceptanceLevel.md) |  | [optional] 
**last_modified** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**source_identifiers** | **List[str]** |  | [optional] 
**v2_acceptance_level** | [**NvdsourceNvdAcceptanceLevel**](NvdsourceNvdAcceptanceLevel.md) |  | [optional] 
**v3_acceptance_level** | [**NvdsourceNvdAcceptanceLevel**](NvdsourceNvdAcceptanceLevel.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.nvdsource_nvd_source import NvdsourceNvdSource

# TODO update the JSON string below
json = "{}"
# create an instance of NvdsourceNvdSource from a JSON string
nvdsource_nvd_source_instance = NvdsourceNvdSource.from_json(json)
# print the JSON string representation of the object
print(NvdsourceNvdSource.to_json())

# convert the object into a dict
nvdsource_nvd_source_dict = nvdsource_nvd_source_instance.to_dict()
# create an instance of NvdsourceNvdSource from a dict
nvdsource_nvd_source_from_dict = NvdsourceNvdSource.from_dict(nvdsource_nvd_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


