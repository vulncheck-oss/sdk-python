# AdvisoryMCvssV40


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_score** | **float** |  | [optional] 
**vector_string** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_m_cvss_v40 import AdvisoryMCvssV40

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMCvssV40 from a JSON string
advisory_m_cvss_v40_instance = AdvisoryMCvssV40.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMCvssV40.to_json())

# convert the object into a dict
advisory_m_cvss_v40_dict = advisory_m_cvss_v40_instance.to_dict()
# create an instance of AdvisoryMCvssV40 from a dict
advisory_m_cvss_v40_from_dict = AdvisoryMCvssV40.from_dict(advisory_m_cvss_v40_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


