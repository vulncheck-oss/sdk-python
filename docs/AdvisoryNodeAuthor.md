# AdvisoryNodeAuthor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**website** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_node_author import AdvisoryNodeAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNodeAuthor from a JSON string
advisory_node_author_instance = AdvisoryNodeAuthor.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNodeAuthor.to_json())

# convert the object into a dict
advisory_node_author_dict = advisory_node_author_instance.to_dict()
# create an instance of AdvisoryNodeAuthor from a dict
advisory_node_author_from_dict = AdvisoryNodeAuthor.from_dict(advisory_node_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


