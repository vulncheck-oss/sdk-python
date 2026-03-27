# BackupFeedItem

backup.FeedItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** |  | [optional] 
**backup_written_at** | **str** |  | [optional] 
**href** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.backup_feed_item import BackupFeedItem

# TODO update the JSON string below
json = "{}"
# create an instance of BackupFeedItem from a JSON string
backup_feed_item_instance = BackupFeedItem.from_json(json)
# print the JSON string representation of the object
print(BackupFeedItem.to_json())

# convert the object into a dict
backup_feed_item_dict = backup_feed_item_instance.to_dict()
# create an instance of BackupFeedItem from a dict
backup_feed_item_from_dict = BackupFeedItem.from_dict(backup_feed_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


