# AdvisoryVMWareAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory_id** | **str** |  | [optional] 
**advisory_url** | **str** |  | [optional] 
**cvssv3_range** | **str** |  | [optional] 
**issue_date** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**synopsis** | **str** |  | [optional] 
**updated_on** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_vm_ware_advisory import AdvisoryVMWareAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVMWareAdvisory from a JSON string
advisory_vm_ware_advisory_instance = AdvisoryVMWareAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVMWareAdvisory.to_json())

# convert the object into a dict
advisory_vm_ware_advisory_dict = advisory_vm_ware_advisory_instance.to_dict()
# create an instance of AdvisoryVMWareAdvisory from a dict
advisory_vm_ware_advisory_from_dict = AdvisoryVMWareAdvisory.from_dict(advisory_vm_ware_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


