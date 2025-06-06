# AdvisoryMCvssV20


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_vector** | **str** |  | [optional] 
**attack_complexity** | **str** |  | [optional] 
**authentication** | **str** |  | [optional] 
**availability_impact** | **str** |  | [optional] 
**base_score** | **float** |  | [optional] 
**confidentiality_impact** | **str** |  | [optional] 
**integrity_impact** | **str** |  | [optional] 
**vector_string** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_m_cvss_v20 import AdvisoryMCvssV20

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMCvssV20 from a JSON string
advisory_m_cvss_v20_instance = AdvisoryMCvssV20.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMCvssV20.to_json())

# convert the object into a dict
advisory_m_cvss_v20_dict = advisory_m_cvss_v20_instance.to_dict()
# create an instance of AdvisoryMCvssV20 from a dict
advisory_m_cvss_v20_from_dict = AdvisoryMCvssV20.from_dict(advisory_m_cvss_v20_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


