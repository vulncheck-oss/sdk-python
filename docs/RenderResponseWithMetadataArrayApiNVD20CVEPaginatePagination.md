# RenderResponseWithMetadataArrayApiNVD20CVEPaginatePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark** | **float** |  | [optional] 
**meta** | [**PaginatePagination**](PaginatePagination.md) |  | [optional] 
**data** | [**List[ApiNVD20CVE]**](ApiNVD20CVE.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.render_response_with_metadata_array_api_nvd20_cve_paginate_pagination import RenderResponseWithMetadataArrayApiNVD20CVEPaginatePagination

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponseWithMetadataArrayApiNVD20CVEPaginatePagination from a JSON string
render_response_with_metadata_array_api_nvd20_cve_paginate_pagination_instance = RenderResponseWithMetadataArrayApiNVD20CVEPaginatePagination.from_json(json)
# print the JSON string representation of the object
print(RenderResponseWithMetadataArrayApiNVD20CVEPaginatePagination.to_json())

# convert the object into a dict
render_response_with_metadata_array_api_nvd20_cve_paginate_pagination_dict = render_response_with_metadata_array_api_nvd20_cve_paginate_pagination_instance.to_dict()
# create an instance of RenderResponseWithMetadataArrayApiNVD20CVEPaginatePagination from a dict
render_response_with_metadata_array_api_nvd20_cve_paginate_pagination_from_dict = RenderResponseWithMetadataArrayApiNVD20CVEPaginatePagination.from_dict(render_response_with_metadata_array_api_nvd20_cve_paginate_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


