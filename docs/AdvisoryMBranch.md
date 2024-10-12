# AdvisoryMBranch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | [**List[AdvisoryMBranch]**](AdvisoryMBranch.md) |  | [optional] 
**full_product_name** | [**List[AdvisoryMFullProductName]**](AdvisoryMFullProductName.md) |  | [optional] 
**items** | [**List[AdvisoryMItem]**](AdvisoryMItem.md) |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **int** | diff | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_m_branch import AdvisoryMBranch

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMBranch from a JSON string
advisory_m_branch_instance = AdvisoryMBranch.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMBranch.to_json())

# convert the object into a dict
advisory_m_branch_dict = advisory_m_branch_instance.to_dict()
# create an instance of AdvisoryMBranch from a dict
advisory_m_branch_from_dict = AdvisoryMBranch.from_dict(advisory_m_branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


