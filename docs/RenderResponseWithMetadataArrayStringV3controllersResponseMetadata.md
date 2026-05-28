# RenderResponseWithMetadataArrayStringV3controllersResponseMetadata

render.ResponseWithMetadata-array_string-v3controllers_ResponseMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark** | **float** | Benchmark is the server-side processing time for the request in seconds. Example: 0.122322 &#x3D; approximately 122 milliseconds | [optional] 
**meta** | [**V3controllersResponseMetadata**](V3controllersResponseMetadata.md) |  | [optional] 
**data** | **List[str]** | Data is the data returned by the endpoint | [optional] 

## Example

```python
from vulncheck_sdk.models.render_response_with_metadata_array_string_v3controllers_response_metadata import RenderResponseWithMetadataArrayStringV3controllersResponseMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponseWithMetadataArrayStringV3controllersResponseMetadata from a JSON string
render_response_with_metadata_array_string_v3controllers_response_metadata_instance = RenderResponseWithMetadataArrayStringV3controllersResponseMetadata.from_json(json)
# print the JSON string representation of the object
print(RenderResponseWithMetadataArrayStringV3controllersResponseMetadata.to_json())

# convert the object into a dict
render_response_with_metadata_array_string_v3controllers_response_metadata_dict = render_response_with_metadata_array_string_v3controllers_response_metadata_instance.to_dict()
# create an instance of RenderResponseWithMetadataArrayStringV3controllersResponseMetadata from a dict
render_response_with_metadata_array_string_v3controllers_response_metadata_from_dict = RenderResponseWithMetadataArrayStringV3controllersResponseMetadata.from_dict(render_response_with_metadata_array_string_v3controllers_response_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


