# AdvisoryMCveMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigner_org_id** | **str** |  | [optional] 
**assigner_short_name** | **str** |  | [optional] 
**cve_id** | **str** |  | [optional] 
**date_published** | **str** |  | [optional] 
**date_reserved** | **str** |  | [optional] 
**date_updated** | **str** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_m_cve_metadata import AdvisoryMCveMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMCveMetadata from a JSON string
advisory_m_cve_metadata_instance = AdvisoryMCveMetadata.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMCveMetadata.to_json())

# convert the object into a dict
advisory_m_cve_metadata_dict = advisory_m_cve_metadata_instance.to_dict()
# create an instance of AdvisoryMCveMetadata from a dict
advisory_m_cve_metadata_from_dict = AdvisoryMCveMetadata.from_dict(advisory_m_cve_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


