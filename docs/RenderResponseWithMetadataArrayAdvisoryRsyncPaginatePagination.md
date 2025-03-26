# RenderResponseWithMetadataArrayAdvisoryRsyncPaginatePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark** | **float** |  | [optional] 
**meta** | [**PaginatePagination**](PaginatePagination.md) |  | [optional] 
**data** | [**List[AdvisoryRsync]**](AdvisoryRsync.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.render_response_with_metadata_array_advisory_rsync_paginate_pagination import RenderResponseWithMetadataArrayAdvisoryRsyncPaginatePagination

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponseWithMetadataArrayAdvisoryRsyncPaginatePagination from a JSON string
render_response_with_metadata_array_advisory_rsync_paginate_pagination_instance = RenderResponseWithMetadataArrayAdvisoryRsyncPaginatePagination.from_json(json)
# print the JSON string representation of the object
print(RenderResponseWithMetadataArrayAdvisoryRsyncPaginatePagination.to_json())

# convert the object into a dict
render_response_with_metadata_array_advisory_rsync_paginate_pagination_dict = render_response_with_metadata_array_advisory_rsync_paginate_pagination_instance.to_dict()
# create an instance of RenderResponseWithMetadataArrayAdvisoryRsyncPaginatePagination from a dict
render_response_with_metadata_array_advisory_rsync_paginate_pagination_from_dict = RenderResponseWithMetadataArrayAdvisoryRsyncPaginatePagination.from_dict(render_response_with_metadata_array_advisory_rsync_paginate_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


