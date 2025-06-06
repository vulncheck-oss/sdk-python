# AdvisoryMCvssV30


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attack_complexity** | **str** |  | [optional] 
**attack_vector** | **str** |  | [optional] 
**availability_impact** | **str** |  | [optional] 
**base_score** | **float** |  | [optional] 
**base_severity** | **str** |  | [optional] 
**confidentiality_impact** | **str** |  | [optional] 
**integrity_impact** | **str** |  | [optional] 
**privileges_required** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 
**user_interaction** | **str** |  | [optional] 
**vector_string** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_m_cvss_v30 import AdvisoryMCvssV30

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMCvssV30 from a JSON string
advisory_m_cvss_v30_instance = AdvisoryMCvssV30.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMCvssV30.to_json())

# convert the object into a dict
advisory_m_cvss_v30_dict = advisory_m_cvss_v30_instance.to_dict()
# create an instance of AdvisoryMCvssV30 from a dict
advisory_m_cvss_v30_from_dict = AdvisoryMCvssV30.from_dict(advisory_m_cvss_v30_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


