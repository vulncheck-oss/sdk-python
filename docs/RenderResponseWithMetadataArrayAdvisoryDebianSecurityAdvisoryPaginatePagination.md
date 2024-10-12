# RenderResponseWithMetadataArrayAdvisoryDebianSecurityAdvisoryPaginatePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark** | **float** |  | [optional] 
**meta** | [**PaginatePagination**](PaginatePagination.md) |  | [optional] 
**data** | [**List[AdvisoryDebianSecurityAdvisory]**](AdvisoryDebianSecurityAdvisory.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.render_response_with_metadata_array_advisory_debian_security_advisory_paginate_pagination import RenderResponseWithMetadataArrayAdvisoryDebianSecurityAdvisoryPaginatePagination

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponseWithMetadataArrayAdvisoryDebianSecurityAdvisoryPaginatePagination from a JSON string
render_response_with_metadata_array_advisory_debian_security_advisory_paginate_pagination_instance = RenderResponseWithMetadataArrayAdvisoryDebianSecurityAdvisoryPaginatePagination.from_json(json)
# print the JSON string representation of the object
print(RenderResponseWithMetadataArrayAdvisoryDebianSecurityAdvisoryPaginatePagination.to_json())

# convert the object into a dict
render_response_with_metadata_array_advisory_debian_security_advisory_paginate_pagination_dict = render_response_with_metadata_array_advisory_debian_security_advisory_paginate_pagination_instance.to_dict()
# create an instance of RenderResponseWithMetadataArrayAdvisoryDebianSecurityAdvisoryPaginatePagination from a dict
render_response_with_metadata_array_advisory_debian_security_advisory_paginate_pagination_from_dict = RenderResponseWithMetadataArrayAdvisoryDebianSecurityAdvisoryPaginatePagination.from_dict(render_response_with_metadata_array_advisory_debian_security_advisory_paginate_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


