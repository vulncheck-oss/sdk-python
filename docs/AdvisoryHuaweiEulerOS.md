# AdvisoryHuaweiEulerOS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**packages** | **str** |  | [optional] 
**products** | **List[str]** |  | [optional] 
**severity** | **str** |  | [optional] 
**synopsis** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_huawei_euler_os import AdvisoryHuaweiEulerOS

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryHuaweiEulerOS from a JSON string
advisory_huawei_euler_os_instance = AdvisoryHuaweiEulerOS.from_json(json)
# print the JSON string representation of the object
print(AdvisoryHuaweiEulerOS.to_json())

# convert the object into a dict
advisory_huawei_euler_os_dict = advisory_huawei_euler_os_instance.to_dict()
# create an instance of AdvisoryHuaweiEulerOS from a dict
advisory_huawei_euler_os_from_dict = AdvisoryHuaweiEulerOS.from_dict(advisory_huawei_euler_os_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


