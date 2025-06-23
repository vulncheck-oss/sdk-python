# AdvisoryTenableResearchAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_tenable_research_advisory import AdvisoryTenableResearchAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryTenableResearchAdvisory from a JSON string
advisory_tenable_research_advisory_instance = AdvisoryTenableResearchAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryTenableResearchAdvisory.to_json())

# convert the object into a dict
advisory_tenable_research_advisory_dict = advisory_tenable_research_advisory_instance.to_dict()
# create an instance of AdvisoryTenableResearchAdvisory from a dict
advisory_tenable_research_advisory_from_dict = AdvisoryTenableResearchAdvisory.from_dict(advisory_tenable_research_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


