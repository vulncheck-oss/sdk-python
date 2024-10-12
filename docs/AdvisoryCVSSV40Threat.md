# AdvisoryCVSSV40Threat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_threat_score** | **float** |  | [optional] 
**base_threat_severity** | **str** |  | [optional] 
**exploit_maturity** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cvssv40_threat import AdvisoryCVSSV40Threat

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCVSSV40Threat from a JSON string
advisory_cvssv40_threat_instance = AdvisoryCVSSV40Threat.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCVSSV40Threat.to_json())

# convert the object into a dict
advisory_cvssv40_threat_dict = advisory_cvssv40_threat_instance.to_dict()
# create an instance of AdvisoryCVSSV40Threat from a dict
advisory_cvssv40_threat_from_dict = AdvisoryCVSSV40Threat.from_dict(advisory_cvssv40_threat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


