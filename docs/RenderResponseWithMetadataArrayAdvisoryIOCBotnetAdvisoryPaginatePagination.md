# RenderResponseWithMetadataArrayAdvisoryIOCBotnetAdvisoryPaginatePagination

render.ResponseWithMetadata-array_advisory_IOCBotnetAdvisory-paginate_Pagination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark** | **float** | Benchmark is the server-side processing time for the request in seconds. Example: 0.122322 &#x3D; approximately 122 milliseconds | [optional] 
**meta** | [**PaginatePagination**](PaginatePagination.md) |  | [optional] 
**data** | [**List[AdvisoryIOCBotnetAdvisory]**](AdvisoryIOCBotnetAdvisory.md) | Data is the data returned by the endpoint | [optional] 

## Example

```python
from vulncheck_sdk.models.render_response_with_metadata_array_advisory_ioc_botnet_advisory_paginate_pagination import RenderResponseWithMetadataArrayAdvisoryIOCBotnetAdvisoryPaginatePagination

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponseWithMetadataArrayAdvisoryIOCBotnetAdvisoryPaginatePagination from a JSON string
render_response_with_metadata_array_advisory_ioc_botnet_advisory_paginate_pagination_instance = RenderResponseWithMetadataArrayAdvisoryIOCBotnetAdvisoryPaginatePagination.from_json(json)
# print the JSON string representation of the object
print(RenderResponseWithMetadataArrayAdvisoryIOCBotnetAdvisoryPaginatePagination.to_json())

# convert the object into a dict
render_response_with_metadata_array_advisory_ioc_botnet_advisory_paginate_pagination_dict = render_response_with_metadata_array_advisory_ioc_botnet_advisory_paginate_pagination_instance.to_dict()
# create an instance of RenderResponseWithMetadataArrayAdvisoryIOCBotnetAdvisoryPaginatePagination from a dict
render_response_with_metadata_array_advisory_ioc_botnet_advisory_paginate_pagination_from_dict = RenderResponseWithMetadataArrayAdvisoryIOCBotnetAdvisoryPaginatePagination.from_dict(render_response_with_metadata_array_advisory_ioc_botnet_advisory_paginate_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


