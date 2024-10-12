# AdvisoryRevision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**number** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_revision import AdvisoryRevision

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRevision from a JSON string
advisory_revision_instance = AdvisoryRevision.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRevision.to_json())

# convert the object into a dict
advisory_revision_dict = advisory_revision_instance.to_dict()
# create an instance of AdvisoryRevision from a dict
advisory_revision_from_dict = AdvisoryRevision.from_dict(advisory_revision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


