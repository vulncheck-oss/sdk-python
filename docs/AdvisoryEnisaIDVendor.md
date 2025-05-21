# AdvisoryEnisaIDVendor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**vendor_name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_enisa_id_vendor import AdvisoryEnisaIDVendor

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryEnisaIDVendor from a JSON string
advisory_enisa_id_vendor_instance = AdvisoryEnisaIDVendor.from_json(json)
# print the JSON string representation of the object
print(AdvisoryEnisaIDVendor.to_json())

# convert the object into a dict
advisory_enisa_id_vendor_dict = advisory_enisa_id_vendor_instance.to_dict()
# create an instance of AdvisoryEnisaIDVendor from a dict
advisory_enisa_id_vendor_from_dict = AdvisoryEnisaIDVendor.from_dict(advisory_enisa_id_vendor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


