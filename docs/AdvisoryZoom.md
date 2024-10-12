# AdvisoryZoom


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**zsb** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_zoom import AdvisoryZoom

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryZoom from a JSON string
advisory_zoom_instance = AdvisoryZoom.from_json(json)
# print the JSON string representation of the object
print(AdvisoryZoom.to_json())

# convert the object into a dict
advisory_zoom_dict = advisory_zoom_instance.to_dict()
# create an instance of AdvisoryZoom from a dict
advisory_zoom_from_dict = AdvisoryZoom.from_dict(advisory_zoom_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


