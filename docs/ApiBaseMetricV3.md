# ApiBaseMetricV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cvss_v3** | [**ApiCVSSV3**](ApiCVSSV3.md) |  | [optional] 
**exploitability_score** | **float** |  | [optional] 
**impact_score** | **float** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_base_metric_v3 import ApiBaseMetricV3

# TODO update the JSON string below
json = "{}"
# create an instance of ApiBaseMetricV3 from a JSON string
api_base_metric_v3_instance = ApiBaseMetricV3.from_json(json)
# print the JSON string representation of the object
print(ApiBaseMetricV3.to_json())

# convert the object into a dict
api_base_metric_v3_dict = api_base_metric_v3_instance.to_dict()
# create an instance of ApiBaseMetricV3 from a dict
api_base_metric_v3_from_dict = ApiBaseMetricV3.from_dict(api_base_metric_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


