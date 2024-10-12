# AdvisoryUnify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_unify import AdvisoryUnify

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryUnify from a JSON string
advisory_unify_instance = AdvisoryUnify.from_json(json)
# print the JSON string representation of the object
print(AdvisoryUnify.to_json())

# convert the object into a dict
advisory_unify_dict = advisory_unify_instance.to_dict()
# create an instance of AdvisoryUnify from a dict
advisory_unify_from_dict = AdvisoryUnify.from_dict(advisory_unify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


