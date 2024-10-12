# AdvisoryAtlassianProducts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **List[str]** |  | [optional] 
**fixed** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_atlassian_products import AdvisoryAtlassianProducts

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAtlassianProducts from a JSON string
advisory_atlassian_products_instance = AdvisoryAtlassianProducts.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAtlassianProducts.to_json())

# convert the object into a dict
advisory_atlassian_products_dict = advisory_atlassian_products_instance.to_dict()
# create an instance of AdvisoryAtlassianProducts from a dict
advisory_atlassian_products_from_dict = AdvisoryAtlassianProducts.from_dict(advisory_atlassian_products_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


