# RenderResponseWithMetadataArrayAdvisoryAssetNotePaginatePagination

render.ResponseWithMetadata-array_advisory_AssetNote-paginate_Pagination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark** | **float** | Benchmark is the server-side processing time for the request in seconds. Example: 0.122322 &#x3D; approximately 122 milliseconds | [optional] 
**meta** | [**PaginatePagination**](PaginatePagination.md) |  | [optional] 
**data** | [**List[AdvisoryAssetNote]**](AdvisoryAssetNote.md) | Data is the data returned by the endpoint | [optional] 

## Example

```python
from vulncheck_sdk.models.render_response_with_metadata_array_advisory_asset_note_paginate_pagination import RenderResponseWithMetadataArrayAdvisoryAssetNotePaginatePagination

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponseWithMetadataArrayAdvisoryAssetNotePaginatePagination from a JSON string
render_response_with_metadata_array_advisory_asset_note_paginate_pagination_instance = RenderResponseWithMetadataArrayAdvisoryAssetNotePaginatePagination.from_json(json)
# print the JSON string representation of the object
print(RenderResponseWithMetadataArrayAdvisoryAssetNotePaginatePagination.to_json())

# convert the object into a dict
render_response_with_metadata_array_advisory_asset_note_paginate_pagination_dict = render_response_with_metadata_array_advisory_asset_note_paginate_pagination_instance.to_dict()
# create an instance of RenderResponseWithMetadataArrayAdvisoryAssetNotePaginatePagination from a dict
render_response_with_metadata_array_advisory_asset_note_paginate_pagination_from_dict = RenderResponseWithMetadataArrayAdvisoryAssetNotePaginatePagination.from_dict(render_response_with_metadata_array_advisory_asset_note_paginate_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


