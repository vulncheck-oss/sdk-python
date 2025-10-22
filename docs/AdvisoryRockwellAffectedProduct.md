# AdvisoryRockwellAffectedProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_catalog_number** | **str** |  | [optional] 
**affected_version** | **str** |  | [optional] 
**corrected_version** | **str** |  | [optional] 
**cve** | **str** |  | [optional] 
**product** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_rockwell_affected_product import AdvisoryRockwellAffectedProduct

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRockwellAffectedProduct from a JSON string
advisory_rockwell_affected_product_instance = AdvisoryRockwellAffectedProduct.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRockwellAffectedProduct.to_json())

# convert the object into a dict
advisory_rockwell_affected_product_dict = advisory_rockwell_affected_product_instance.to_dict()
# create an instance of AdvisoryRockwellAffectedProduct from a dict
advisory_rockwell_affected_product_from_dict = AdvisoryRockwellAffectedProduct.from_dict(advisory_rockwell_affected_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


