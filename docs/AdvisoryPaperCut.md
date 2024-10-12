# AdvisoryPaperCut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_paper_cut import AdvisoryPaperCut

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPaperCut from a JSON string
advisory_paper_cut_instance = AdvisoryPaperCut.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPaperCut.to_json())

# convert the object into a dict
advisory_paper_cut_dict = advisory_paper_cut_instance.to_dict()
# create an instance of AdvisoryPaperCut from a dict
advisory_paper_cut_from_dict = AdvisoryPaperCut.from_dict(advisory_paper_cut_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


