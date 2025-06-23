# RenderResponseWithMetadataArrayAdvisoryJuniperPaginatePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark** | **float** |  | [optional] 
**meta** | [**PaginatePagination**](PaginatePagination.md) |  | [optional] 
**data** | [**List[AdvisoryJuniper]**](AdvisoryJuniper.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.render_response_with_metadata_array_advisory_juniper_paginate_pagination import RenderResponseWithMetadataArrayAdvisoryJuniperPaginatePagination

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponseWithMetadataArrayAdvisoryJuniperPaginatePagination from a JSON string
render_response_with_metadata_array_advisory_juniper_paginate_pagination_instance = RenderResponseWithMetadataArrayAdvisoryJuniperPaginatePagination.from_json(json)
# print the JSON string representation of the object
print(RenderResponseWithMetadataArrayAdvisoryJuniperPaginatePagination.to_json())

# convert the object into a dict
render_response_with_metadata_array_advisory_juniper_paginate_pagination_dict = render_response_with_metadata_array_advisory_juniper_paginate_pagination_instance.to_dict()
# create an instance of RenderResponseWithMetadataArrayAdvisoryJuniperPaginatePagination from a dict
render_response_with_metadata_array_advisory_juniper_paginate_pagination_from_dict = RenderResponseWithMetadataArrayAdvisoryJuniperPaginatePagination.from_dict(render_response_with_metadata_array_advisory_juniper_paginate_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


