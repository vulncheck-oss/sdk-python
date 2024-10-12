# RenderResponseWithMetadataArrayAdvisorySpringPaginatePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark** | **float** |  | [optional] 
**meta** | [**PaginatePagination**](PaginatePagination.md) |  | [optional] 
**data** | [**List[AdvisorySpring]**](AdvisorySpring.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.render_response_with_metadata_array_advisory_spring_paginate_pagination import RenderResponseWithMetadataArrayAdvisorySpringPaginatePagination

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponseWithMetadataArrayAdvisorySpringPaginatePagination from a JSON string
render_response_with_metadata_array_advisory_spring_paginate_pagination_instance = RenderResponseWithMetadataArrayAdvisorySpringPaginatePagination.from_json(json)
# print the JSON string representation of the object
print(RenderResponseWithMetadataArrayAdvisorySpringPaginatePagination.to_json())

# convert the object into a dict
render_response_with_metadata_array_advisory_spring_paginate_pagination_dict = render_response_with_metadata_array_advisory_spring_paginate_pagination_instance.to_dict()
# create an instance of RenderResponseWithMetadataArrayAdvisorySpringPaginatePagination from a dict
render_response_with_metadata_array_advisory_spring_paginate_pagination_from_dict = RenderResponseWithMetadataArrayAdvisorySpringPaginatePagination.from_dict(render_response_with_metadata_array_advisory_spring_paginate_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


