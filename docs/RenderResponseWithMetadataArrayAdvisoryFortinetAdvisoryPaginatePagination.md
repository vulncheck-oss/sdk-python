# RenderResponseWithMetadataArrayAdvisoryFortinetAdvisoryPaginatePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark** | **float** |  | [optional] 
**meta** | [**PaginatePagination**](PaginatePagination.md) |  | [optional] 
**data** | [**List[AdvisoryFortinetAdvisory]**](AdvisoryFortinetAdvisory.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.render_response_with_metadata_array_advisory_fortinet_advisory_paginate_pagination import RenderResponseWithMetadataArrayAdvisoryFortinetAdvisoryPaginatePagination

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponseWithMetadataArrayAdvisoryFortinetAdvisoryPaginatePagination from a JSON string
render_response_with_metadata_array_advisory_fortinet_advisory_paginate_pagination_instance = RenderResponseWithMetadataArrayAdvisoryFortinetAdvisoryPaginatePagination.from_json(json)
# print the JSON string representation of the object
print(RenderResponseWithMetadataArrayAdvisoryFortinetAdvisoryPaginatePagination.to_json())

# convert the object into a dict
render_response_with_metadata_array_advisory_fortinet_advisory_paginate_pagination_dict = render_response_with_metadata_array_advisory_fortinet_advisory_paginate_pagination_instance.to_dict()
# create an instance of RenderResponseWithMetadataArrayAdvisoryFortinetAdvisoryPaginatePagination from a dict
render_response_with_metadata_array_advisory_fortinet_advisory_paginate_pagination_from_dict = RenderResponseWithMetadataArrayAdvisoryFortinetAdvisoryPaginatePagination.from_dict(render_response_with_metadata_array_advisory_fortinet_advisory_paginate_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


