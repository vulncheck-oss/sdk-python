# AdvisoryProductSpecificDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**display_value** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_product_specific_detail import AdvisoryProductSpecificDetail

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryProductSpecificDetail from a JSON string
advisory_product_specific_detail_instance = AdvisoryProductSpecificDetail.from_json(json)
# print the JSON string representation of the object
print(AdvisoryProductSpecificDetail.to_json())

# convert the object into a dict
advisory_product_specific_detail_dict = advisory_product_specific_detail_instance.to_dict()
# create an instance of AdvisoryProductSpecificDetail from a dict
advisory_product_specific_detail_from_dict = AdvisoryProductSpecificDetail.from_dict(advisory_product_specific_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


