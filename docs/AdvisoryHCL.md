# AdvisoryHCL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_hcl import AdvisoryHCL

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryHCL from a JSON string
advisory_hcl_instance = AdvisoryHCL.from_json(json)
# print the JSON string representation of the object
print(AdvisoryHCL.to_json())

# convert the object into a dict
advisory_hcl_dict = advisory_hcl_instance.to_dict()
# create an instance of AdvisoryHCL from a dict
advisory_hcl_from_dict = AdvisoryHCL.from_dict(advisory_hcl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


