# AdvisoryZDIVendor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**uri** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_zdi_vendor import AdvisoryZDIVendor

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryZDIVendor from a JSON string
advisory_zdi_vendor_instance = AdvisoryZDIVendor.from_json(json)
# print the JSON string representation of the object
print(AdvisoryZDIVendor.to_json())

# convert the object into a dict
advisory_zdi_vendor_dict = advisory_zdi_vendor_instance.to_dict()
# create an instance of AdvisoryZDIVendor from a dict
advisory_zdi_vendor_from_dict = AdvisoryZDIVendor.from_dict(advisory_zdi_vendor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


