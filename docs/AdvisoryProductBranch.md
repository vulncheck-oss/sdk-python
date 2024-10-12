# AdvisoryProductBranch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branches** | [**List[AdvisoryProductBranch]**](AdvisoryProductBranch.md) |  | [optional] 
**category** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**product** | [**AdvisoryProduct**](AdvisoryProduct.md) |  | [optional] 
**relationships** | [**List[AdvisoryCSAFRelationship]**](AdvisoryCSAFRelationship.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_product_branch import AdvisoryProductBranch

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryProductBranch from a JSON string
advisory_product_branch_instance = AdvisoryProductBranch.from_json(json)
# print the JSON string representation of the object
print(AdvisoryProductBranch.to_json())

# convert the object into a dict
advisory_product_branch_dict = advisory_product_branch_instance.to_dict()
# create an instance of AdvisoryProductBranch from a dict
advisory_product_branch_from_dict = AdvisoryProductBranch.from_dict(advisory_product_branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


