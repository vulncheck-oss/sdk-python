# AdvisoryHuawei


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**sa_number** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_huawei import AdvisoryHuawei

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryHuawei from a JSON string
advisory_huawei_instance = AdvisoryHuawei.from_json(json)
# print the JSON string representation of the object
print(AdvisoryHuawei.to_json())

# convert the object into a dict
advisory_huawei_dict = advisory_huawei_instance.to_dict()
# create an instance of AdvisoryHuawei from a dict
advisory_huawei_from_dict = AdvisoryHuawei.from_dict(advisory_huawei_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


