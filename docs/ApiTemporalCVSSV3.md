# ApiTemporalCVSSV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exploit_code_maturity** | **str** |  | [optional] 
**remediation_level** | **str** |  | [optional] 
**report_confidence** | **str** |  | [optional] 
**temporal_score** | **float** |  | [optional] 
**vector_string** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_temporal_cvssv3 import ApiTemporalCVSSV3

# TODO update the JSON string below
json = "{}"
# create an instance of ApiTemporalCVSSV3 from a JSON string
api_temporal_cvssv3_instance = ApiTemporalCVSSV3.from_json(json)
# print the JSON string representation of the object
print(ApiTemporalCVSSV3.to_json())

# convert the object into a dict
api_temporal_cvssv3_dict = api_temporal_cvssv3_instance.to_dict()
# create an instance of ApiTemporalCVSSV3 from a dict
api_temporal_cvssv3_from_dict = ApiTemporalCVSSV3.from_dict(api_temporal_cvssv3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


