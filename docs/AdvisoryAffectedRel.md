# AdvisoryAffectedRel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory** | **str** |  | [optional] 
**cpe** | **str** |  | [optional] 
**package** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 
**release_date** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_affected_rel import AdvisoryAffectedRel

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAffectedRel from a JSON string
advisory_affected_rel_instance = AdvisoryAffectedRel.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAffectedRel.to_json())

# convert the object into a dict
advisory_affected_rel_dict = advisory_affected_rel_instance.to_dict()
# create an instance of AdvisoryAffectedRel from a dict
advisory_affected_rel_from_dict = AdvisoryAffectedRel.from_dict(advisory_affected_rel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


