# ApiBaseMetricV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ac_insuf_info** | **bool** |  | [optional] 
**cvss_v2** | [**ApiCVSSV2**](ApiCVSSV2.md) |  | [optional] 
**exploitability_score** | **float** |  | [optional] 
**impact_score** | **float** |  | [optional] 
**obtain_all_privilege** | **bool** |  | [optional] 
**obtain_other_privilege** | **bool** |  | [optional] 
**obtain_user_privilege** | **bool** |  | [optional] 
**severity** | **str** |  | [optional] 
**user_interaction_required** | **bool** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_base_metric_v2 import ApiBaseMetricV2

# TODO update the JSON string below
json = "{}"
# create an instance of ApiBaseMetricV2 from a JSON string
api_base_metric_v2_instance = ApiBaseMetricV2.from_json(json)
# print the JSON string representation of the object
print(ApiBaseMetricV2.to_json())

# convert the object into a dict
api_base_metric_v2_dict = api_base_metric_v2_instance.to_dict()
# create an instance of ApiBaseMetricV2 from a dict
api_base_metric_v2_from_dict = ApiBaseMetricV2.from_dict(api_base_metric_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


