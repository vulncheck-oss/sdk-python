# ApiImpactExtended


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_metric_v2** | [**ApiBaseMetricV2**](ApiBaseMetricV2.md) |  | [optional] 
**base_metric_v3** | [**ApiBaseMetricV3**](ApiBaseMetricV3.md) |  | [optional] 
**corrected_base_metric_v3** | [**ApiBaseMetricV3**](ApiBaseMetricV3.md) |  | [optional] 
**epss** | [**ApiEPSS**](ApiEPSS.md) |  | [optional] 
**metric_v40** | [**AdvisoryCVSSV40**](AdvisoryCVSSV40.md) |  | [optional] 
**ssvc** | [**List[ApiSSVC]**](ApiSSVC.md) |  | [optional] 
**temporal_metric_v2** | [**ApiTemporalMetricV2**](ApiTemporalMetricV2.md) |  | [optional] 
**temporal_metric_v3** | [**ApiTemporalMetricV3**](ApiTemporalMetricV3.md) |  | [optional] 
**temporal_v3_corrected** | [**ApiTemporalMetricV3**](ApiTemporalMetricV3.md) |  | [optional] 
**threat_metric_v40** | [**AdvisoryCVSSV40Threat**](AdvisoryCVSSV40Threat.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_impact_extended import ApiImpactExtended

# TODO update the JSON string below
json = "{}"
# create an instance of ApiImpactExtended from a JSON string
api_impact_extended_instance = ApiImpactExtended.from_json(json)
# print the JSON string representation of the object
print(ApiImpactExtended.to_json())

# convert the object into a dict
api_impact_extended_dict = api_impact_extended_instance.to_dict()
# create an instance of ApiImpactExtended from a dict
api_impact_extended_from_dict = ApiImpactExtended.from_dict(api_impact_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


