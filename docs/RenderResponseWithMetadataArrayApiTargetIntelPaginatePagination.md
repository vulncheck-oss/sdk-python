# RenderResponseWithMetadataArrayApiTargetIntelPaginatePagination

render.ResponseWithMetadata-array_api_TargetIntel-paginate_Pagination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark** | **float** |  | [optional] 
**meta** | [**PaginatePagination**](PaginatePagination.md) |  | [optional] 
**data** | [**List[ApiTargetIntel]**](ApiTargetIntel.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.render_response_with_metadata_array_api_target_intel_paginate_pagination import RenderResponseWithMetadataArrayApiTargetIntelPaginatePagination

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponseWithMetadataArrayApiTargetIntelPaginatePagination from a JSON string
render_response_with_metadata_array_api_target_intel_paginate_pagination_instance = RenderResponseWithMetadataArrayApiTargetIntelPaginatePagination.from_json(json)
# print the JSON string representation of the object
print(RenderResponseWithMetadataArrayApiTargetIntelPaginatePagination.to_json())

# convert the object into a dict
render_response_with_metadata_array_api_target_intel_paginate_pagination_dict = render_response_with_metadata_array_api_target_intel_paginate_pagination_instance.to_dict()
# create an instance of RenderResponseWithMetadataArrayApiTargetIntelPaginatePagination from a dict
render_response_with_metadata_array_api_target_intel_paginate_pagination_from_dict = RenderResponseWithMetadataArrayApiTargetIntelPaginatePagination.from_dict(render_response_with_metadata_array_api_target_intel_paginate_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


