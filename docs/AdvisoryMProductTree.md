# AdvisoryMProductTree


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | [**List[AdvisoryMBranch]**](AdvisoryMBranch.md) |  | [optional] 
**full_product_name** | [**List[AdvisoryMFullProductName]**](AdvisoryMFullProductName.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_m_product_tree import AdvisoryMProductTree

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMProductTree from a JSON string
advisory_m_product_tree_instance = AdvisoryMProductTree.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMProductTree.to_json())

# convert the object into a dict
advisory_m_product_tree_dict = advisory_m_product_tree_instance.to_dict()
# create an instance of AdvisoryMProductTree from a dict
advisory_m_product_tree_from_dict = AdvisoryMProductTree.from_dict(advisory_m_product_tree_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


