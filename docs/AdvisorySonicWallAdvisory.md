# AdvisorySonicWallAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory_id** | **str** |  | [optional] 
**affected_products** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss** | **str** |  | [optional] 
**cvss_vector** | **str** |  | [optional] 
**cvss_version** | **float** |  | [optional] 
**cwe** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**impact** | **str** |  | [optional] 
**is_workaround_available** | **bool** |  | [optional] 
**last_updated_when** | **str** |  | [optional] 
**published_when** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vuln_status** | **str** |  | [optional] 
**vulnerable_products_list** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_sonic_wall_advisory import AdvisorySonicWallAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySonicWallAdvisory from a JSON string
advisory_sonic_wall_advisory_instance = AdvisorySonicWallAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisorySonicWallAdvisory.to_json())

# convert the object into a dict
advisory_sonic_wall_advisory_dict = advisory_sonic_wall_advisory_instance.to_dict()
# create an instance of AdvisorySonicWallAdvisory from a dict
advisory_sonic_wall_advisory_from_dict = AdvisorySonicWallAdvisory.from_dict(advisory_sonic_wall_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


