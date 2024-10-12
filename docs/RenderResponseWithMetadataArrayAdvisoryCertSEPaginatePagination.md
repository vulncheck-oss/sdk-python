# RenderResponseWithMetadataArrayAdvisoryCertSEPaginatePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark** | **float** |  | [optional] 
**meta** | [**PaginatePagination**](PaginatePagination.md) |  | [optional] 
**data** | [**List[AdvisoryCertSE]**](AdvisoryCertSE.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.render_response_with_metadata_array_advisory_cert_se_paginate_pagination import RenderResponseWithMetadataArrayAdvisoryCertSEPaginatePagination

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponseWithMetadataArrayAdvisoryCertSEPaginatePagination from a JSON string
render_response_with_metadata_array_advisory_cert_se_paginate_pagination_instance = RenderResponseWithMetadataArrayAdvisoryCertSEPaginatePagination.from_json(json)
# print the JSON string representation of the object
print(RenderResponseWithMetadataArrayAdvisoryCertSEPaginatePagination.to_json())

# convert the object into a dict
render_response_with_metadata_array_advisory_cert_se_paginate_pagination_dict = render_response_with_metadata_array_advisory_cert_se_paginate_pagination_instance.to_dict()
# create an instance of RenderResponseWithMetadataArrayAdvisoryCertSEPaginatePagination from a dict
render_response_with_metadata_array_advisory_cert_se_paginate_pagination_from_dict = RenderResponseWithMetadataArrayAdvisoryCertSEPaginatePagination.from_dict(render_response_with_metadata_array_advisory_cert_se_paginate_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


