# AdvisoryAutodesk


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
from vulncheck_sdk.models.advisory_autodesk import AdvisoryAutodesk

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAutodesk from a JSON string
advisory_autodesk_instance = AdvisoryAutodesk.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAutodesk.to_json())

# convert the object into a dict
advisory_autodesk_dict = advisory_autodesk_instance.to_dict()
# create an instance of AdvisoryAutodesk from a dict
advisory_autodesk_from_dict = AdvisoryAutodesk.from_dict(advisory_autodesk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


