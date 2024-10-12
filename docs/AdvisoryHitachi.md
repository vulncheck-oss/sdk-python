# AdvisoryHitachi


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_products** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed_products** | **str** |  | [optional] 
**hitachi_id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_hitachi import AdvisoryHitachi

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryHitachi from a JSON string
advisory_hitachi_instance = AdvisoryHitachi.from_json(json)
# print the JSON string representation of the object
print(AdvisoryHitachi.to_json())

# convert the object into a dict
advisory_hitachi_dict = advisory_hitachi_instance.to_dict()
# create an instance of AdvisoryHitachi from a dict
advisory_hitachi_from_dict = AdvisoryHitachi.from_dict(advisory_hitachi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


