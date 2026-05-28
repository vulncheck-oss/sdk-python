# AdvisoryCirclCveMetadata

advisory.CirclCveMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigner_org_id** | **str** |  | [optional] 
**assigner_short_name** | **str** |  | [optional] 
**cve_id** | **str** |  | [optional] 
**date_published** | **str** |  | [optional] 
**date_rejected** | **str** |  | [optional] 
**date_reserved** | **str** |  | [optional] 
**date_updated** | **str** |  | [optional] 
**requester_user_id** | **str** |  | [optional] 
**serial** | **int** |  | [optional] 
**state** | **str** |  | [optional] 
**vuln_id** | **str** |  | [optional] 
**vulnerabilitylookup_history** | **List[List[str]]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_circl_cve_metadata import AdvisoryCirclCveMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCirclCveMetadata from a JSON string
advisory_circl_cve_metadata_instance = AdvisoryCirclCveMetadata.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCirclCveMetadata.to_json())

# convert the object into a dict
advisory_circl_cve_metadata_dict = advisory_circl_cve_metadata_instance.to_dict()
# create an instance of AdvisoryCirclCveMetadata from a dict
advisory_circl_cve_metadata_from_dict = AdvisoryCirclCveMetadata.from_dict(advisory_circl_cve_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


