# AdvisoryNetApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**impact** | **str** |  | [optional] 
**ntap** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_net_app import AdvisoryNetApp

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNetApp from a JSON string
advisory_net_app_instance = AdvisoryNetApp.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNetApp.to_json())

# convert the object into a dict
advisory_net_app_dict = advisory_net_app_instance.to_dict()
# create an instance of AdvisoryNetApp from a dict
advisory_net_app_from_dict = AdvisoryNetApp.from_dict(advisory_net_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


