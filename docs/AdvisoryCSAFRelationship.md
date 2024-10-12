# AdvisoryCSAFRelationship


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**full_product_name** | [**AdvisoryProduct**](AdvisoryProduct.md) |  | [optional] 
**product_reference** | **str** |  | [optional] 
**relates_to_product_reference** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_csaf_relationship import AdvisoryCSAFRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCSAFRelationship from a JSON string
advisory_csaf_relationship_instance = AdvisoryCSAFRelationship.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCSAFRelationship.to_json())

# convert the object into a dict
advisory_csaf_relationship_dict = advisory_csaf_relationship_instance.to_dict()
# create an instance of AdvisoryCSAFRelationship from a dict
advisory_csaf_relationship_from_dict = AdvisoryCSAFRelationship.from_dict(advisory_csaf_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


