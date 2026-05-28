# RenderResponseWithMetadataArrayAdvisorySymfonyPaginatePagination

render.ResponseWithMetadata-array_advisory_Symfony-paginate_Pagination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark** | **float** | Benchmark is the server-side processing time for the request in seconds. Example: 0.122322 &#x3D; approximately 122 milliseconds | [optional] 
**meta** | [**PaginatePagination**](PaginatePagination.md) |  | [optional] 
**data** | [**List[AdvisorySymfony]**](AdvisorySymfony.md) | Data is the data returned by the endpoint | [optional] 

## Example

```python
from vulncheck_sdk.models.render_response_with_metadata_array_advisory_symfony_paginate_pagination import RenderResponseWithMetadataArrayAdvisorySymfonyPaginatePagination

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponseWithMetadataArrayAdvisorySymfonyPaginatePagination from a JSON string
render_response_with_metadata_array_advisory_symfony_paginate_pagination_instance = RenderResponseWithMetadataArrayAdvisorySymfonyPaginatePagination.from_json(json)
# print the JSON string representation of the object
print(RenderResponseWithMetadataArrayAdvisorySymfonyPaginatePagination.to_json())

# convert the object into a dict
render_response_with_metadata_array_advisory_symfony_paginate_pagination_dict = render_response_with_metadata_array_advisory_symfony_paginate_pagination_instance.to_dict()
# create an instance of RenderResponseWithMetadataArrayAdvisorySymfonyPaginatePagination from a dict
render_response_with_metadata_array_advisory_symfony_paginate_pagination_from_dict = RenderResponseWithMetadataArrayAdvisorySymfonyPaginatePagination.from_dict(render_response_with_metadata_array_advisory_symfony_paginate_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


