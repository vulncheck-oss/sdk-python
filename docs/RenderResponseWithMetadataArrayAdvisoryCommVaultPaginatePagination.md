# RenderResponseWithMetadataArrayAdvisoryCommVaultPaginatePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark** | **float** |  | [optional] 
**meta** | [**PaginatePagination**](PaginatePagination.md) |  | [optional] 
**data** | [**List[AdvisoryCommVault]**](AdvisoryCommVault.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.render_response_with_metadata_array_advisory_comm_vault_paginate_pagination import RenderResponseWithMetadataArrayAdvisoryCommVaultPaginatePagination

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponseWithMetadataArrayAdvisoryCommVaultPaginatePagination from a JSON string
render_response_with_metadata_array_advisory_comm_vault_paginate_pagination_instance = RenderResponseWithMetadataArrayAdvisoryCommVaultPaginatePagination.from_json(json)
# print the JSON string representation of the object
print(RenderResponseWithMetadataArrayAdvisoryCommVaultPaginatePagination.to_json())

# convert the object into a dict
render_response_with_metadata_array_advisory_comm_vault_paginate_pagination_dict = render_response_with_metadata_array_advisory_comm_vault_paginate_pagination_instance.to_dict()
# create an instance of RenderResponseWithMetadataArrayAdvisoryCommVaultPaginatePagination from a dict
render_response_with_metadata_array_advisory_comm_vault_paginate_pagination_from_dict = RenderResponseWithMetadataArrayAdvisoryCommVaultPaginatePagination.from_dict(render_response_with_metadata_array_advisory_comm_vault_paginate_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


