# RenderResponseWithMetadataArrayAdvisoryQualysQIDPaginatePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark** | **float** |  | [optional] 
**meta** | [**PaginatePagination**](PaginatePagination.md) |  | [optional] 
**data** | [**List[AdvisoryQualysQID]**](AdvisoryQualysQID.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.render_response_with_metadata_array_advisory_qualys_qid_paginate_pagination import RenderResponseWithMetadataArrayAdvisoryQualysQIDPaginatePagination

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponseWithMetadataArrayAdvisoryQualysQIDPaginatePagination from a JSON string
render_response_with_metadata_array_advisory_qualys_qid_paginate_pagination_instance = RenderResponseWithMetadataArrayAdvisoryQualysQIDPaginatePagination.from_json(json)
# print the JSON string representation of the object
print(RenderResponseWithMetadataArrayAdvisoryQualysQIDPaginatePagination.to_json())

# convert the object into a dict
render_response_with_metadata_array_advisory_qualys_qid_paginate_pagination_dict = render_response_with_metadata_array_advisory_qualys_qid_paginate_pagination_instance.to_dict()
# create an instance of RenderResponseWithMetadataArrayAdvisoryQualysQIDPaginatePagination from a dict
render_response_with_metadata_array_advisory_qualys_qid_paginate_pagination_from_dict = RenderResponseWithMetadataArrayAdvisoryQualysQIDPaginatePagination.from_dict(render_response_with_metadata_array_advisory_qualys_qid_paginate_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


