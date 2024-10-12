# AdvisoryGHNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package** | [**AdvisoryGHPackage**](AdvisoryGHPackage.md) |  | [optional] 
**severity** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**vulnerable_version_range** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_gh_node import AdvisoryGHNode

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGHNode from a JSON string
advisory_gh_node_instance = AdvisoryGHNode.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGHNode.to_json())

# convert the object into a dict
advisory_gh_node_dict = advisory_gh_node_instance.to_dict()
# create an instance of AdvisoryGHNode from a dict
advisory_gh_node_from_dict = AdvisoryGHNode.from_dict(advisory_gh_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


