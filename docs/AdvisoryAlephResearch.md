# AdvisoryAlephResearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_aleph_research import AdvisoryAlephResearch

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAlephResearch from a JSON string
advisory_aleph_research_instance = AdvisoryAlephResearch.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAlephResearch.to_json())

# convert the object into a dict
advisory_aleph_research_dict = advisory_aleph_research_instance.to_dict()
# create an instance of AdvisoryAlephResearch from a dict
advisory_aleph_research_from_dict = AdvisoryAlephResearch.from_dict(advisory_aleph_research_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


