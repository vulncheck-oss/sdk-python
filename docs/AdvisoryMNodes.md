# AdvisoryMNodes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpe_match** | [**List[AdvisoryMCPEMatch]**](AdvisoryMCPEMatch.md) |  | [optional] 
**negate** | **bool** |  | [optional] 
**operator** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_m_nodes import AdvisoryMNodes

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMNodes from a JSON string
advisory_m_nodes_instance = AdvisoryMNodes.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMNodes.to_json())

# convert the object into a dict
advisory_m_nodes_dict = advisory_m_nodes_instance.to_dict()
# create an instance of AdvisoryMNodes from a dict
advisory_m_nodes_from_dict = AdvisoryMNodes.from_dict(advisory_m_nodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


