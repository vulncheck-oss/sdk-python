# RenderResponseWithMetadataArrayAdvisoryMitelPaginatePagination

render.ResponseWithMetadata-array_advisory_Mitel-paginate_Pagination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark** | **float** | Benchmark is the server-side processing time for the request in seconds. Example: 0.122322 &#x3D; approximately 122 milliseconds | [optional] 
**meta** | [**PaginatePagination**](PaginatePagination.md) |  | [optional] 
**data** | [**List[AdvisoryMitel]**](AdvisoryMitel.md) | Data is the data returned by the endpoint | [optional] 

## Example

```python
from vulncheck_sdk.models.render_response_with_metadata_array_advisory_mitel_paginate_pagination import RenderResponseWithMetadataArrayAdvisoryMitelPaginatePagination

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponseWithMetadataArrayAdvisoryMitelPaginatePagination from a JSON string
render_response_with_metadata_array_advisory_mitel_paginate_pagination_instance = RenderResponseWithMetadataArrayAdvisoryMitelPaginatePagination.from_json(json)
# print the JSON string representation of the object
print(RenderResponseWithMetadataArrayAdvisoryMitelPaginatePagination.to_json())

# convert the object into a dict
render_response_with_metadata_array_advisory_mitel_paginate_pagination_dict = render_response_with_metadata_array_advisory_mitel_paginate_pagination_instance.to_dict()
# create an instance of RenderResponseWithMetadataArrayAdvisoryMitelPaginatePagination from a dict
render_response_with_metadata_array_advisory_mitel_paginate_pagination_from_dict = RenderResponseWithMetadataArrayAdvisoryMitelPaginatePagination.from_dict(render_response_with_metadata_array_advisory_mitel_paginate_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


