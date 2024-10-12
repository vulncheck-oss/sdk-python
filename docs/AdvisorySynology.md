# AdvisorySynology


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_products** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**last_updated** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**severity** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_synology import AdvisorySynology

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySynology from a JSON string
advisory_synology_instance = AdvisorySynology.from_json(json)
# print the JSON string representation of the object
print(AdvisorySynology.to_json())

# convert the object into a dict
advisory_synology_dict = advisory_synology_instance.to_dict()
# create an instance of AdvisorySynology from a dict
advisory_synology_from_dict = AdvisorySynology.from_dict(advisory_synology_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


