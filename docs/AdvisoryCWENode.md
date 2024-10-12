# AdvisoryCWENode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cweid** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cwe_node import AdvisoryCWENode

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCWENode from a JSON string
advisory_cwe_node_instance = AdvisoryCWENode.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCWENode.to_json())

# convert the object into a dict
advisory_cwe_node_dict = advisory_cwe_node_instance.to_dict()
# create an instance of AdvisoryCWENode from a dict
advisory_cwe_node_from_dict = AdvisoryCWENode.from_dict(advisory_cwe_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


