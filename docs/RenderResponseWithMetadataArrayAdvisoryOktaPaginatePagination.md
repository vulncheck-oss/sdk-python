# RenderResponseWithMetadataArrayAdvisoryOktaPaginatePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benchmark** | **float** |  | [optional] 
**meta** | [**PaginatePagination**](PaginatePagination.md) |  | [optional] 
**data** | [**List[AdvisoryOkta]**](AdvisoryOkta.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.render_response_with_metadata_array_advisory_okta_paginate_pagination import RenderResponseWithMetadataArrayAdvisoryOktaPaginatePagination

# TODO update the JSON string below
json = "{}"
# create an instance of RenderResponseWithMetadataArrayAdvisoryOktaPaginatePagination from a JSON string
render_response_with_metadata_array_advisory_okta_paginate_pagination_instance = RenderResponseWithMetadataArrayAdvisoryOktaPaginatePagination.from_json(json)
# print the JSON string representation of the object
print(RenderResponseWithMetadataArrayAdvisoryOktaPaginatePagination.to_json())

# convert the object into a dict
render_response_with_metadata_array_advisory_okta_paginate_pagination_dict = render_response_with_metadata_array_advisory_okta_paginate_pagination_instance.to_dict()
# create an instance of RenderResponseWithMetadataArrayAdvisoryOktaPaginatePagination from a dict
render_response_with_metadata_array_advisory_okta_paginate_pagination_from_dict = RenderResponseWithMetadataArrayAdvisoryOktaPaginatePagination.from_dict(render_response_with_metadata_array_advisory_okta_paginate_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


