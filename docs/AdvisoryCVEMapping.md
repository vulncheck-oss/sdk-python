# AdvisoryCVEMapping

advisory.CVEMapping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cve_mapping import AdvisoryCVEMapping

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCVEMapping from a JSON string
advisory_cve_mapping_instance = AdvisoryCVEMapping.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCVEMapping.to_json())

# convert the object into a dict
advisory_cve_mapping_dict = advisory_cve_mapping_instance.to_dict()
# create an instance of AdvisoryCVEMapping from a dict
advisory_cve_mapping_from_dict = AdvisoryCVEMapping.from_dict(advisory_cve_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


