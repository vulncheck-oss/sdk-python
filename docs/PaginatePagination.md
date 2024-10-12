# PaginatePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cursor** | **str** | Cursor for the current page | [optional] 
**first_item** | **int** | First and last Item | [optional] 
**index** | **str** | The requested index | [optional] 
**last_item** | **int** |  | [optional] 
**limit** | **int** | Per-Page limit | [optional] 
**matches** | [**List[PaginateMatch]**](PaginateMatch.md) |  | [optional] 
**max_pages** | **int** |  | [optional] 
**next_cursor** | **str** | Cursor for the next page | [optional] 
**opensearch_query** | **object** | NOTE: swaggertype tag is needed so that swaggo/swag run from &#x60;make openapi&#x60; does not die in a fire | [optional] 
**order** | **str** |  | [optional] 
**page** | **int** | The current Page number | [optional] 
**pages** | **List[str]** |  | [optional] 
**parameters** | [**List[PaginateParam]**](PaginateParam.md) |  | [optional] 
**show_pages** | **bool** |  | [optional] 
**show_query** | **bool** |  | [optional] 
**sort** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 
**total_documents** | **int** | The total number of items | [optional] 
**total_pages** | **int** | The total number of pages | [optional] 
**warnings** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.paginate_pagination import PaginatePagination

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatePagination from a JSON string
paginate_pagination_instance = PaginatePagination.from_json(json)
# print the JSON string representation of the object
print(PaginatePagination.to_json())

# convert the object into a dict
paginate_pagination_dict = paginate_pagination_instance.to_dict()
# create an instance of PaginatePagination from a dict
paginate_pagination_from_dict = PaginatePagination.from_dict(paginate_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


