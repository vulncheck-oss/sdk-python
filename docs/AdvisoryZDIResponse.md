# AdvisoryZDIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 
**vendor** | [**AdvisoryZDIResponseVendor**](AdvisoryZDIResponseVendor.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_zdi_response import AdvisoryZDIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryZDIResponse from a JSON string
advisory_zdi_response_instance = AdvisoryZDIResponse.from_json(json)
# print the JSON string representation of the object
print(AdvisoryZDIResponse.to_json())

# convert the object into a dict
advisory_zdi_response_dict = advisory_zdi_response_instance.to_dict()
# create an instance of AdvisoryZDIResponse from a dict
advisory_zdi_response_from_dict = AdvisoryZDIResponse.from_dict(advisory_zdi_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


