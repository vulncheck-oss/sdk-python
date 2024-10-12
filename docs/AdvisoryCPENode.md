# AdvisoryCPENode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpe_match** | [**List[AdvisoryCPEMatch]**](AdvisoryCPEMatch.md) |  | [optional] 
**negate** | **bool** |  | [optional] 
**operator** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cpe_node import AdvisoryCPENode

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCPENode from a JSON string
advisory_cpe_node_instance = AdvisoryCPENode.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCPENode.to_json())

# convert the object into a dict
advisory_cpe_node_dict = advisory_cpe_node_instance.to_dict()
# create an instance of AdvisoryCPENode from a dict
advisory_cpe_node_from_dict = AdvisoryCPENode.from_dict(advisory_cpe_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


