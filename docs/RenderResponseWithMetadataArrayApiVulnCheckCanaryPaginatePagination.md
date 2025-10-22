# RenderResponseWithMetadataArrayApiVulnCheckCanaryPaginatePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark** | **float** |  | [optional] 
**meta** | [**PaginatePagination**](PaginatePagination.md) |  | [optional] 
**data** | [**List[ApiVulnCheckCanary]**](ApiVulnCheckCanary.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.render_response_with_metadata_array_api_vuln_check_canary_paginate_pagination import RenderResponseWithMetadataArrayApiVulnCheckCanaryPaginatePagination

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponseWithMetadataArrayApiVulnCheckCanaryPaginatePagination from a JSON string
render_response_with_metadata_array_api_vuln_check_canary_paginate_pagination_instance = RenderResponseWithMetadataArrayApiVulnCheckCanaryPaginatePagination.from_json(json)
# print the JSON string representation of the object
print(RenderResponseWithMetadataArrayApiVulnCheckCanaryPaginatePagination.to_json())

# convert the object into a dict
render_response_with_metadata_array_api_vuln_check_canary_paginate_pagination_dict = render_response_with_metadata_array_api_vuln_check_canary_paginate_pagination_instance.to_dict()
# create an instance of RenderResponseWithMetadataArrayApiVulnCheckCanaryPaginatePagination from a dict
render_response_with_metadata_array_api_vuln_check_canary_paginate_pagination_from_dict = RenderResponseWithMetadataArrayApiVulnCheckCanaryPaginatePagination.from_dict(render_response_with_metadata_array_api_vuln_check_canary_paginate_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


