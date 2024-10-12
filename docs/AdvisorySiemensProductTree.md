# AdvisorySiemensProductTree


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branches** | [**List[AdvisorySiemensBranch]**](AdvisorySiemensBranch.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_siemens_product_tree import AdvisorySiemensProductTree

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySiemensProductTree from a JSON string
advisory_siemens_product_tree_instance = AdvisorySiemensProductTree.from_json(json)
# print the JSON string representation of the object
print(AdvisorySiemensProductTree.to_json())

# convert the object into a dict
advisory_siemens_product_tree_dict = advisory_siemens_product_tree_instance.to_dict()
# create an instance of AdvisorySiemensProductTree from a dict
advisory_siemens_product_tree_from_dict = AdvisorySiemensProductTree.from_dict(advisory_siemens_product_tree_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


