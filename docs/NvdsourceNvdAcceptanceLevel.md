# NvdsourceNvdAcceptanceLevel

nvdsource.NvdAcceptanceLevel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**last_modified** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.nvdsource_nvd_acceptance_level import NvdsourceNvdAcceptanceLevel

# TODO update the JSON string below
json = "{}"
# create an instance of NvdsourceNvdAcceptanceLevel from a JSON string
nvdsource_nvd_acceptance_level_instance = NvdsourceNvdAcceptanceLevel.from_json(json)
# print the JSON string representation of the object
print(NvdsourceNvdAcceptanceLevel.to_json())

# convert the object into a dict
nvdsource_nvd_acceptance_level_dict = nvdsource_nvd_acceptance_level_instance.to_dict()
# create an instance of NvdsourceNvdAcceptanceLevel from a dict
nvdsource_nvd_acceptance_level_from_dict = NvdsourceNvdAcceptanceLevel.from_dict(nvdsource_nvd_acceptance_level_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


