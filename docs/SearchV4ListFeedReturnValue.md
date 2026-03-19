# SearchV4ListFeedReturnValue

search.V4ListFeedReturnValue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SearchV4FeedItem]**](SearchV4FeedItem.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.search_v4_list_feed_return_value import SearchV4ListFeedReturnValue

# TODO update the JSON string below
json = "{}"
# create an instance of SearchV4ListFeedReturnValue from a JSON string
search_v4_list_feed_return_value_instance = SearchV4ListFeedReturnValue.from_json(json)
# print the JSON string representation of the object
print(SearchV4ListFeedReturnValue.to_json())

# convert the object into a dict
search_v4_list_feed_return_value_dict = search_v4_list_feed_return_value_instance.to_dict()
# create an instance of SearchV4ListFeedReturnValue from a dict
search_v4_list_feed_return_value_from_dict = SearchV4ListFeedReturnValue.from_dict(search_v4_list_feed_return_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


