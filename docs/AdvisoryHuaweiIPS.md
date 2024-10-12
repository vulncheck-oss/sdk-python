# AdvisoryHuaweiIPS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cnnvd** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**date_updated** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**threat_id** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_huawei_ips import AdvisoryHuaweiIPS

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryHuaweiIPS from a JSON string
advisory_huawei_ips_instance = AdvisoryHuaweiIPS.from_json(json)
# print the JSON string representation of the object
print(AdvisoryHuaweiIPS.to_json())

# convert the object into a dict
advisory_huawei_ips_dict = advisory_huawei_ips_instance.to_dict()
# create an instance of AdvisoryHuaweiIPS from a dict
advisory_huawei_ips_from_dict = AdvisoryHuaweiIPS.from_dict(advisory_huawei_ips_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


