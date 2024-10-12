# ApiTemporalCVSSV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exploitability** | **str** |  | [optional] 
**remediation_level** | **str** |  | [optional] 
**report_confidence** | **str** |  | [optional] 
**temporal_score** | **float** |  | [optional] 
**vector_string** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_temporal_cvssv2 import ApiTemporalCVSSV2

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTemporalCVSSV2 from a JSON string
api_temporal_cvssv2_instance = ApiTemporalCVSSV2.from_json(json)
# print the JSON string representation of the object
print(ApiTemporalCVSSV2.to_json())

# convert the object into a dict
api_temporal_cvssv2_dict = api_temporal_cvssv2_instance.to_dict()
# create an instance of ApiTemporalCVSSV2 from a dict
api_temporal_cvssv2_from_dict = ApiTemporalCVSSV2.from_dict(api_temporal_cvssv2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


