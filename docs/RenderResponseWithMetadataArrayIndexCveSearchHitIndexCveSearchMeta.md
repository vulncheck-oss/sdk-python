# RenderResponseWithMetadataArrayIndexCveSearchHitIndexCveSearchMeta

render.ResponseWithMetadata-array_index_CveSearchHit-index_CveSearchMeta

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark** | **float** | Benchmark is the server-side processing time for the request in seconds. Example: 0.122322 &#x3D; approximately 122 milliseconds | [optional] 
**meta** | [**IndexCveSearchMeta**](IndexCveSearchMeta.md) |  | [optional] 
**data** | [**List[IndexCveSearchHit]**](IndexCveSearchHit.md) | Data is the data returned by the endpoint | [optional] 

## Example

```python
from vulncheck_sdk.models.render_response_with_metadata_array_index_cve_search_hit_index_cve_search_meta import RenderResponseWithMetadataArrayIndexCveSearchHitIndexCveSearchMeta

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponseWithMetadataArrayIndexCveSearchHitIndexCveSearchMeta from a JSON string
render_response_with_metadata_array_index_cve_search_hit_index_cve_search_meta_instance = RenderResponseWithMetadataArrayIndexCveSearchHitIndexCveSearchMeta.from_json(json)
# print the JSON string representation of the object
print(RenderResponseWithMetadataArrayIndexCveSearchHitIndexCveSearchMeta.to_json())

# convert the object into a dict
render_response_with_metadata_array_index_cve_search_hit_index_cve_search_meta_dict = render_response_with_metadata_array_index_cve_search_hit_index_cve_search_meta_instance.to_dict()
# create an instance of RenderResponseWithMetadataArrayIndexCveSearchHitIndexCveSearchMeta from a dict
render_response_with_metadata_array_index_cve_search_hit_index_cve_search_meta_from_dict = RenderResponseWithMetadataArrayIndexCveSearchHitIndexCveSearchMeta.from_dict(render_response_with_metadata_array_index_cve_search_hit_index_cve_search_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


