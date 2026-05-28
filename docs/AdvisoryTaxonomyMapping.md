# AdvisoryTaxonomyMapping

advisory.TaxonomyMapping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy_name** | **str** |  | [optional] 
**taxonomy_relations** | [**List[AdvisoryTaxonomyRelation]**](AdvisoryTaxonomyRelation.md) |  | [optional] 
**taxonomy_version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_taxonomy_mapping import AdvisoryTaxonomyMapping

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryTaxonomyMapping from a JSON string
advisory_taxonomy_mapping_instance = AdvisoryTaxonomyMapping.from_json(json)
# print the JSON string representation of the object
print(AdvisoryTaxonomyMapping.to_json())

# convert the object into a dict
advisory_taxonomy_mapping_dict = advisory_taxonomy_mapping_instance.to_dict()
# create an instance of AdvisoryTaxonomyMapping from a dict
advisory_taxonomy_mapping_from_dict = AdvisoryTaxonomyMapping.from_dict(advisory_taxonomy_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


