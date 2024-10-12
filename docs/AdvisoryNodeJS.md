# AdvisoryNodeJS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_node_js import AdvisoryNodeJS

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNodeJS from a JSON string
advisory_node_js_instance = AdvisoryNodeJS.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNodeJS.to_json())

# convert the object into a dict
advisory_node_js_dict = advisory_node_js_instance.to_dict()
# create an instance of AdvisoryNodeJS from a dict
advisory_node_js_from_dict = AdvisoryNodeJS.from_dict(advisory_node_js_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


