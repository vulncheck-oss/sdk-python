# AdvisoryNVD20Node


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpe_match** | [**List[AdvisoryNVD20CVECPEMatch]**](AdvisoryNVD20CVECPEMatch.md) |  | [optional] 
**negate** | **bool** |  | [optional] 
**operator** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_nvd20_node import AdvisoryNVD20Node

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNVD20Node from a JSON string
advisory_nvd20_node_instance = AdvisoryNVD20Node.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNVD20Node.to_json())

# convert the object into a dict
advisory_nvd20_node_dict = advisory_nvd20_node_instance.to_dict()
# create an instance of AdvisoryNVD20Node from a dict
advisory_nvd20_node_from_dict = AdvisoryNVD20Node.from_dict(advisory_nvd20_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


