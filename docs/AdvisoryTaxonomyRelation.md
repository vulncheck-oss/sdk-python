# AdvisoryTaxonomyRelation

advisory.TaxonomyRelation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relationship_name** | **str** |  | [optional] 
**relationship_value** | **str** |  | [optional] 
**taxonomy_id** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_taxonomy_relation import AdvisoryTaxonomyRelation

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryTaxonomyRelation from a JSON string
advisory_taxonomy_relation_instance = AdvisoryTaxonomyRelation.from_json(json)
# print the JSON string representation of the object
print(AdvisoryTaxonomyRelation.to_json())

# convert the object into a dict
advisory_taxonomy_relation_dict = advisory_taxonomy_relation_instance.to_dict()
# create an instance of AdvisoryTaxonomyRelation from a dict
advisory_taxonomy_relation_from_dict = AdvisoryTaxonomyRelation.from_dict(advisory_taxonomy_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


