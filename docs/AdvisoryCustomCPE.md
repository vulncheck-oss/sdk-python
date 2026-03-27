# AdvisoryCustomCPE

advisory.CustomCPE

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mcpeapplicability** | [**AdvisoryMCPEApplicability**](AdvisoryMCPEApplicability.md) |  | [optional] 
**string_value** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_custom_cpe import AdvisoryCustomCPE

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCustomCPE from a JSON string
advisory_custom_cpe_instance = AdvisoryCustomCPE.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCustomCPE.to_json())

# convert the object into a dict
advisory_custom_cpe_dict = advisory_custom_cpe_instance.to_dict()
# create an instance of AdvisoryCustomCPE from a dict
advisory_custom_cpe_from_dict = AdvisoryCustomCPE.from_dict(advisory_custom_cpe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


