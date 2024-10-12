# AdvisorySolarWindsAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_products** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss_score** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed_version** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_solar_winds_advisory import AdvisorySolarWindsAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySolarWindsAdvisory from a JSON string
advisory_solar_winds_advisory_instance = AdvisorySolarWindsAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisorySolarWindsAdvisory.to_json())

# convert the object into a dict
advisory_solar_winds_advisory_dict = advisory_solar_winds_advisory_instance.to_dict()
# create an instance of AdvisorySolarWindsAdvisory from a dict
advisory_solar_winds_advisory_from_dict = AdvisorySolarWindsAdvisory.from_dict(advisory_solar_winds_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


