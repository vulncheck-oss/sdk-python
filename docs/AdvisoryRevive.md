# AdvisoryRevive


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_revive import AdvisoryRevive

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRevive from a JSON string
advisory_revive_instance = AdvisoryRevive.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRevive.to_json())

# convert the object into a dict
advisory_revive_dict = advisory_revive_instance.to_dict()
# create an instance of AdvisoryRevive from a dict
advisory_revive_from_dict = AdvisoryRevive.from_dict(advisory_revive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


