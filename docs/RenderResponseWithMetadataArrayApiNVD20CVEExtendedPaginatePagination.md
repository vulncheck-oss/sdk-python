# RenderResponseWithMetadataArrayApiNVD20CVEExtendedPaginatePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark** | **float** |  | [optional] 
**meta** | [**PaginatePagination**](PaginatePagination.md) |  | [optional] 
**data** | [**List[ApiNVD20CVEExtended]**](ApiNVD20CVEExtended.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.render_response_with_metadata_array_api_nvd20_cve_extended_paginate_pagination import RenderResponseWithMetadataArrayApiNVD20CVEExtendedPaginatePagination

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponseWithMetadataArrayApiNVD20CVEExtendedPaginatePagination from a JSON string
render_response_with_metadata_array_api_nvd20_cve_extended_paginate_pagination_instance = RenderResponseWithMetadataArrayApiNVD20CVEExtendedPaginatePagination.from_json(json)
# print the JSON string representation of the object
print(RenderResponseWithMetadataArrayApiNVD20CVEExtendedPaginatePagination.to_json())

# convert the object into a dict
render_response_with_metadata_array_api_nvd20_cve_extended_paginate_pagination_dict = render_response_with_metadata_array_api_nvd20_cve_extended_paginate_pagination_instance.to_dict()
# create an instance of RenderResponseWithMetadataArrayApiNVD20CVEExtendedPaginatePagination from a dict
render_response_with_metadata_array_api_nvd20_cve_extended_paginate_pagination_from_dict = RenderResponseWithMetadataArrayApiNVD20CVEExtendedPaginatePagination.from_dict(render_response_with_metadata_array_api_nvd20_cve_extended_paginate_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


