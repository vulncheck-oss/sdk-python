# AdvisoryOpenStack


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affects** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_open_stack import AdvisoryOpenStack

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOpenStack from a JSON string
advisory_open_stack_instance = AdvisoryOpenStack.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOpenStack.to_json())

# convert the object into a dict
advisory_open_stack_dict = advisory_open_stack_instance.to_dict()
# create an instance of AdvisoryOpenStack from a dict
advisory_open_stack_from_dict = AdvisoryOpenStack.from_dict(advisory_open_stack_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


