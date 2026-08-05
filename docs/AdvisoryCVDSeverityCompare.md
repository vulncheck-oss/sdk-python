# AdvisoryCVDSeverityCompare

advisory.CVDSeverityCompare

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claude** | **str** |  | [optional] 
**maintainer** | **str** |  | [optional] 
**security_research_firm** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cvd_severity_compare import AdvisoryCVDSeverityCompare

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCVDSeverityCompare from a JSON string
advisory_cvd_severity_compare_instance = AdvisoryCVDSeverityCompare.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCVDSeverityCompare.to_json())

# convert the object into a dict
advisory_cvd_severity_compare_dict = advisory_cvd_severity_compare_instance.to_dict()
# create an instance of AdvisoryCVDSeverityCompare from a dict
advisory_cvd_severity_compare_from_dict = AdvisoryCVDSeverityCompare.from_dict(advisory_cvd_severity_compare_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


