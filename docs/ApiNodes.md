# ApiNodes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[ApiNodes]**](ApiNodes.md) |  | [optional] 
**cpe_match** | [**List[ApiCPEMatch]**](ApiCPEMatch.md) |  | [optional] 
**operator** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nodes import ApiNodes

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNodes from a JSON string
api_nodes_instance = ApiNodes.from_json(json)
# print the JSON string representation of the object
print(ApiNodes.to_json())

# convert the object into a dict
api_nodes_dict = api_nodes_instance.to_dict()
# create an instance of ApiNodes from a dict
api_nodes_from_dict = ApiNodes.from_dict(api_nodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


