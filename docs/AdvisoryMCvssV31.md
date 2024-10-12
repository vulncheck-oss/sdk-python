# AdvisoryMCvssV31


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_score** | **float** |  | [optional] 
**base_severity** | **str** |  | [optional] 
**vector_string** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_m_cvss_v31 import AdvisoryMCvssV31

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMCvssV31 from a JSON string
advisory_m_cvss_v31_instance = AdvisoryMCvssV31.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMCvssV31.to_json())

# convert the object into a dict
advisory_m_cvss_v31_dict = advisory_m_cvss_v31_instance.to_dict()
# create an instance of AdvisoryMCvssV31 from a dict
advisory_m_cvss_v31_from_dict = AdvisoryMCvssV31.from_dict(advisory_m_cvss_v31_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


