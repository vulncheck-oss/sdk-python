# AdvisoryRockyCve


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cvss3_base_score** | **str** |  | [optional] 
**cvss3_scoring_vector** | **str** |  | [optional] 
**cwe** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**source_by** | **str** |  | [optional] 
**source_link** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_rocky_cve import AdvisoryRockyCve

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRockyCve from a JSON string
advisory_rocky_cve_instance = AdvisoryRockyCve.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRockyCve.to_json())

# convert the object into a dict
advisory_rocky_cve_dict = advisory_rocky_cve_instance.to_dict()
# create an instance of AdvisoryRockyCve from a dict
advisory_rocky_cve_from_dict = AdvisoryRockyCve.from_dict(advisory_rocky_cve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


