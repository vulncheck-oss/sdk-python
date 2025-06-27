# AdvisoryVendorRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_ref** | **str** |  | [optional] 
**vendor_ref_url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_vendor_ref import AdvisoryVendorRef

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVendorRef from a JSON string
advisory_vendor_ref_instance = AdvisoryVendorRef.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVendorRef.to_json())

# convert the object into a dict
advisory_vendor_ref_dict = advisory_vendor_ref_instance.to_dict()
# create an instance of AdvisoryVendorRef from a dict
advisory_vendor_ref_from_dict = AdvisoryVendorRef.from_dict(advisory_vendor_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


