# V3controllersResponseMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpe** | **str** |  | [optional] 
**cpe_struct** | [**ApiCPE**](ApiCPE.md) |  | [optional] 
**timestamp** | **str** |  | [optional] 
**total_documents** | **int** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.v3controllers_response_metadata import V3controllersResponseMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of V3controllersResponseMetadata from a JSON string
v3controllers_response_metadata_instance = V3controllersResponseMetadata.from_json(json)
# print the JSON string representation of the object
print(V3controllersResponseMetadata.to_json())

# convert the object into a dict
v3controllers_response_metadata_dict = v3controllers_response_metadata_instance.to_dict()
# create an instance of V3controllersResponseMetadata from a dict
v3controllers_response_metadata_from_dict = V3controllersResponseMetadata.from_dict(v3controllers_response_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


