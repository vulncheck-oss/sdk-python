# ApiTemporalMetricV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cvss_v3** | [**ApiTemporalCVSSV3**](ApiTemporalCVSSV3.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_temporal_metric_v3 import ApiTemporalMetricV3

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTemporalMetricV3 from a JSON string
api_temporal_metric_v3_instance = ApiTemporalMetricV3.from_json(json)
# print the JSON string representation of the object
print(ApiTemporalMetricV3.to_json())

# convert the object into a dict
api_temporal_metric_v3_dict = api_temporal_metric_v3_instance.to_dict()
# create an instance of ApiTemporalMetricV3 from a dict
api_temporal_metric_v3_from_dict = ApiTemporalMetricV3.from_dict(api_temporal_metric_v3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


