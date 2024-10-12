# AdvisoryAvaya


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory_number** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**last_revised** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_avaya import AdvisoryAvaya

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAvaya from a JSON string
advisory_avaya_instance = AdvisoryAvaya.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAvaya.to_json())

# convert the object into a dict
advisory_avaya_dict = advisory_avaya_instance.to_dict()
# create an instance of AdvisoryAvaya from a dict
advisory_avaya_from_dict = AdvisoryAvaya.from_dict(advisory_avaya_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


