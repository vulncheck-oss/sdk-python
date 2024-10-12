# AdvisoryProductTree


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relationships** | [**List[AdvisoryRelationship]**](AdvisoryRelationship.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_product_tree import AdvisoryProductTree

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryProductTree from a JSON string
advisory_product_tree_instance = AdvisoryProductTree.from_json(json)
# print the JSON string representation of the object
print(AdvisoryProductTree.to_json())

# convert the object into a dict
advisory_product_tree_dict = advisory_product_tree_instance.to_dict()
# create an instance of AdvisoryProductTree from a dict
advisory_product_tree_from_dict = AdvisoryProductTree.from_dict(advisory_product_tree_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


