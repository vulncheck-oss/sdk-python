# ApiNVD20ThreatAssociatedBaseMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_score** | **float** |  | [optional] 
**source** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_threat_associated_base_metric import ApiNVD20ThreatAssociatedBaseMetric

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20ThreatAssociatedBaseMetric from a JSON string
api_nvd20_threat_associated_base_metric_instance = ApiNVD20ThreatAssociatedBaseMetric.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20ThreatAssociatedBaseMetric.to_json())

# convert the object into a dict
api_nvd20_threat_associated_base_metric_dict = api_nvd20_threat_associated_base_metric_instance.to_dict()
# create an instance of ApiNVD20ThreatAssociatedBaseMetric from a dict
api_nvd20_threat_associated_base_metric_from_dict = ApiNVD20ThreatAssociatedBaseMetric.from_dict(api_nvd20_threat_associated_base_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


