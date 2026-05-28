# RenderResponseWithMetadataSearchResponsesSearchResponseMetadata

render.ResponseWithMetadata-search_Responses-search_ResponseMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark** | **float** | Benchmark is the server-side processing time for the request in seconds. Example: 0.122322 &#x3D; approximately 122 milliseconds | [optional] 
**meta** | [**SearchResponseMetadata**](SearchResponseMetadata.md) |  | [optional] 
**data** | [**List[SearchResponseDataOut]**](SearchResponseDataOut.md) | Data is the data returned by the endpoint | [optional] 

## Example

```python
from vulncheck_sdk.models.render_response_with_metadata_search_responses_search_response_metadata import RenderResponseWithMetadataSearchResponsesSearchResponseMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponseWithMetadataSearchResponsesSearchResponseMetadata from a JSON string
render_response_with_metadata_search_responses_search_response_metadata_instance = RenderResponseWithMetadataSearchResponsesSearchResponseMetadata.from_json(json)
# print the JSON string representation of the object
print(RenderResponseWithMetadataSearchResponsesSearchResponseMetadata.to_json())

# convert the object into a dict
render_response_with_metadata_search_responses_search_response_metadata_dict = render_response_with_metadata_search_responses_search_response_metadata_instance.to_dict()
# create an instance of RenderResponseWithMetadataSearchResponsesSearchResponseMetadata from a dict
render_response_with_metadata_search_responses_search_response_metadata_from_dict = RenderResponseWithMetadataSearchResponsesSearchResponseMetadata.from_dict(render_response_with_metadata_search_responses_search_response_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


