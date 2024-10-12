# RenderResponseWithMetadataArrayAdvisoryElasticPaginatePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark** | **float** |  | [optional] 
**meta** | [**PaginatePagination**](PaginatePagination.md) |  | [optional] 
**data** | [**List[AdvisoryElastic]**](AdvisoryElastic.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.render_response_with_metadata_array_advisory_elastic_paginate_pagination import RenderResponseWithMetadataArrayAdvisoryElasticPaginatePagination

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponseWithMetadataArrayAdvisoryElasticPaginatePagination from a JSON string
render_response_with_metadata_array_advisory_elastic_paginate_pagination_instance = RenderResponseWithMetadataArrayAdvisoryElasticPaginatePagination.from_json(json)
# print the JSON string representation of the object
print(RenderResponseWithMetadataArrayAdvisoryElasticPaginatePagination.to_json())

# convert the object into a dict
render_response_with_metadata_array_advisory_elastic_paginate_pagination_dict = render_response_with_metadata_array_advisory_elastic_paginate_pagination_instance.to_dict()
# create an instance of RenderResponseWithMetadataArrayAdvisoryElasticPaginatePagination from a dict
render_response_with_metadata_array_advisory_elastic_paginate_pagination_from_dict = RenderResponseWithMetadataArrayAdvisoryElasticPaginatePagination.from_dict(render_response_with_metadata_array_advisory_elastic_paginate_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


