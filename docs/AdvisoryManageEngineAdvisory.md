# AdvisoryManageEngineAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**manage_engine** | [**AdvisoryManageEngine**](AdvisoryManageEngine.md) |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_manage_engine_advisory import AdvisoryManageEngineAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryManageEngineAdvisory from a JSON string
advisory_manage_engine_advisory_instance = AdvisoryManageEngineAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryManageEngineAdvisory.to_json())

# convert the object into a dict
advisory_manage_engine_advisory_dict = advisory_manage_engine_advisory_instance.to_dict()
# create an instance of AdvisoryManageEngineAdvisory from a dict
advisory_manage_engine_advisory_from_dict = AdvisoryManageEngineAdvisory.from_dict(advisory_manage_engine_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


