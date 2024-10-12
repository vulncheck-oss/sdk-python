# ApiImpact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_metric_v2** | [**ApiBaseMetricV2**](ApiBaseMetricV2.md) |  | [optional] 
**base_metric_v3** | [**ApiBaseMetricV3**](ApiBaseMetricV3.md) |  | [optional] 
**metric_v40** | [**AdvisoryCVSSV40**](AdvisoryCVSSV40.md) | this isn&#39;t called baseMetric, because it can contain other metrics -- typically supplemental metrics | [optional] 

## Example

```python
from vulncheck_sdk.models.api_impact import ApiImpact

# TODO update the JSON string below
json = "{}"
# create an instance of ApiImpact from a JSON string
api_impact_instance = ApiImpact.from_json(json)
# print the JSON string representation of the object
print(ApiImpact.to_json())

# convert the object into a dict
api_impact_dict = api_impact_instance.to_dict()
# create an instance of ApiImpact from a dict
api_impact_from_dict = ApiImpact.from_dict(api_impact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


