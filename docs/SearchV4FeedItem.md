# SearchV4FeedItem

search.V4FeedItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.search_v4_feed_item import SearchV4FeedItem

# TODO update the JSON string below
json = "{}"
# create an instance of SearchV4FeedItem from a JSON string
search_v4_feed_item_instance = SearchV4FeedItem.from_json(json)
# print the JSON string representation of the object
print(SearchV4FeedItem.to_json())

# convert the object into a dict
search_v4_feed_item_dict = search_v4_feed_item_instance.to_dict()
# create an instance of SearchV4FeedItem from a dict
search_v4_feed_item_from_dict = SearchV4FeedItem.from_dict(search_v4_feed_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


