# AdvisoryAtlassianAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_version** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**detailed_summary** | **str** | overloading in places with &#39;RiskAssessment&#39; and other places with &#39;Description&#39; | [optional] 
**fixed_version** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**products** | **List[str]** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**release_date** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_atlassian_advisory import AdvisoryAtlassianAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAtlassianAdvisory from a JSON string
advisory_atlassian_advisory_instance = AdvisoryAtlassianAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAtlassianAdvisory.to_json())

# convert the object into a dict
advisory_atlassian_advisory_dict = advisory_atlassian_advisory_instance.to_dict()
# create an instance of AdvisoryAtlassianAdvisory from a dict
advisory_atlassian_advisory_from_dict = AdvisoryAtlassianAdvisory.from_dict(advisory_atlassian_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


