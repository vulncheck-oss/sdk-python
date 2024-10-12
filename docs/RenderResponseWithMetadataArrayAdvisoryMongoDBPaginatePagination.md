# RenderResponseWithMetadataArrayAdvisoryMongoDBPaginatePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark** | **float** |  | [optional] 
**meta** | [**PaginatePagination**](PaginatePagination.md) |  | [optional] 
**data** | [**List[AdvisoryMongoDB]**](AdvisoryMongoDB.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.render_response_with_metadata_array_advisory_mongo_db_paginate_pagination import RenderResponseWithMetadataArrayAdvisoryMongoDBPaginatePagination

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponseWithMetadataArrayAdvisoryMongoDBPaginatePagination from a JSON string
render_response_with_metadata_array_advisory_mongo_db_paginate_pagination_instance = RenderResponseWithMetadataArrayAdvisoryMongoDBPaginatePagination.from_json(json)
# print the JSON string representation of the object
print(RenderResponseWithMetadataArrayAdvisoryMongoDBPaginatePagination.to_json())

# convert the object into a dict
render_response_with_metadata_array_advisory_mongo_db_paginate_pagination_dict = render_response_with_metadata_array_advisory_mongo_db_paginate_pagination_instance.to_dict()
# create an instance of RenderResponseWithMetadataArrayAdvisoryMongoDBPaginatePagination from a dict
render_response_with_metadata_array_advisory_mongo_db_paginate_pagination_from_dict = RenderResponseWithMetadataArrayAdvisoryMongoDBPaginatePagination.from_dict(render_response_with_metadata_array_advisory_mongo_db_paginate_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


