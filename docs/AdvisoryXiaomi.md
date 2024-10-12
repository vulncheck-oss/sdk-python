# AdvisoryXiaomi


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**internal_id** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**summary_cn** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**title_cn** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_xiaomi import AdvisoryXiaomi

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryXiaomi from a JSON string
advisory_xiaomi_instance = AdvisoryXiaomi.from_json(json)
# print the JSON string representation of the object
print(AdvisoryXiaomi.to_json())

# convert the object into a dict
advisory_xiaomi_dict = advisory_xiaomi_instance.to_dict()
# create an instance of AdvisoryXiaomi from a dict
advisory_xiaomi_from_dict = AdvisoryXiaomi.from_dict(advisory_xiaomi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


