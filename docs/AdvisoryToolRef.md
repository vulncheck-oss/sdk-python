# AdvisoryToolRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_added** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_tool_ref import AdvisoryToolRef

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryToolRef from a JSON string
advisory_tool_ref_instance = AdvisoryToolRef.from_json(json)
# print the JSON string representation of the object
print(AdvisoryToolRef.to_json())

# convert the object into a dict
advisory_tool_ref_dict = advisory_tool_ref_instance.to_dict()
# create an instance of AdvisoryToolRef from a dict
advisory_tool_ref_from_dict = AdvisoryToolRef.from_dict(advisory_tool_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


