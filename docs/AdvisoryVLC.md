# AdvisoryVLC


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_vlc import AdvisoryVLC

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVLC from a JSON string
advisory_vlc_instance = AdvisoryVLC.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVLC.to_json())

# convert the object into a dict
advisory_vlc_dict = advisory_vlc_instance.to_dict()
# create an instance of AdvisoryVLC from a dict
advisory_vlc_from_dict = AdvisoryVLC.from_dict(advisory_vlc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


