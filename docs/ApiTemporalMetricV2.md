# ApiTemporalMetricV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cvss_v2** | [**ApiTemporalCVSSV2**](ApiTemporalCVSSV2.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_temporal_metric_v2 import ApiTemporalMetricV2

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTemporalMetricV2 from a JSON string
api_temporal_metric_v2_instance = ApiTemporalMetricV2.from_json(json)
# print the JSON string representation of the object
print(ApiTemporalMetricV2.to_json())

# convert the object into a dict
api_temporal_metric_v2_dict = api_temporal_metric_v2_instance.to_dict()
# create an instance of ApiTemporalMetricV2 from a dict
api_temporal_metric_v2_from_dict = ApiTemporalMetricV2.from_dict(api_temporal_metric_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


