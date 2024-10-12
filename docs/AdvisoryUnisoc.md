# AdvisoryUnisoc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_vector** | **str** |  | [optional] 
**affected_chipsets** | **str** |  | [optional] 
**affected_software** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**rating** | **str** |  | [optional] 
**score** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**technology** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vulnerability** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_unisoc import AdvisoryUnisoc

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryUnisoc from a JSON string
advisory_unisoc_instance = AdvisoryUnisoc.from_json(json)
# print the JSON string representation of the object
print(AdvisoryUnisoc.to_json())

# convert the object into a dict
advisory_unisoc_dict = advisory_unisoc_instance.to_dict()
# create an instance of AdvisoryUnisoc from a dict
advisory_unisoc_from_dict = AdvisoryUnisoc.from_dict(advisory_unisoc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


