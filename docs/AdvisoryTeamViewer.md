# AdvisoryTeamViewer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulletin_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss_score** | **str** |  | [optional] 
**cvss_vector** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_team_viewer import AdvisoryTeamViewer

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryTeamViewer from a JSON string
advisory_team_viewer_instance = AdvisoryTeamViewer.from_json(json)
# print the JSON string representation of the object
print(AdvisoryTeamViewer.to_json())

# convert the object into a dict
advisory_team_viewer_dict = advisory_team_viewer_instance.to_dict()
# create an instance of AdvisoryTeamViewer from a dict
advisory_team_viewer_from_dict = AdvisoryTeamViewer.from_dict(advisory_team_viewer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


