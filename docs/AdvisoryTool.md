# AdvisoryTool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**references** | [**List[AdvisoryToolRef]**](AdvisoryToolRef.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_tool import AdvisoryTool

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryTool from a JSON string
advisory_tool_instance = AdvisoryTool.from_json(json)
# print the JSON string representation of the object
print(AdvisoryTool.to_json())

# convert the object into a dict
advisory_tool_dict = advisory_tool_instance.to_dict()
# create an instance of AdvisoryTool from a dict
advisory_tool_from_dict = AdvisoryTool.from_dict(advisory_tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


