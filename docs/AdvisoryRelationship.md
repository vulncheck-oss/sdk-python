# AdvisoryRelationship


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_reference** | **str** |  | [optional] 
**relates_to_product_reference** | **str** |  | [optional] 
**relation_type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_relationship import AdvisoryRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRelationship from a JSON string
advisory_relationship_instance = AdvisoryRelationship.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRelationship.to_json())

# convert the object into a dict
advisory_relationship_dict = advisory_relationship_instance.to_dict()
# create an instance of AdvisoryRelationship from a dict
advisory_relationship_from_dict = AdvisoryRelationship.from_dict(advisory_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


