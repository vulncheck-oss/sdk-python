# AdvisoryJuniper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss3_score** | **str** |  | [optional] 
**cvss3_vector** | **str** |  | [optional] 
**cvss4_score** | **str** |  | [optional] 
**cvss4_vector** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_juniper import AdvisoryJuniper

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryJuniper from a JSON string
advisory_juniper_instance = AdvisoryJuniper.from_json(json)
# print the JSON string representation of the object
print(AdvisoryJuniper.to_json())

# convert the object into a dict
advisory_juniper_dict = advisory_juniper_instance.to_dict()
# create an instance of AdvisoryJuniper from a dict
advisory_juniper_from_dict = AdvisoryJuniper.from_dict(advisory_juniper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


