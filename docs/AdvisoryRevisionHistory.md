# AdvisoryRevisionHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_revision_history import AdvisoryRevisionHistory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRevisionHistory from a JSON string
advisory_revision_history_instance = AdvisoryRevisionHistory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRevisionHistory.to_json())

# convert the object into a dict
advisory_revision_history_dict = advisory_revision_history_instance.to_dict()
# create an instance of AdvisoryRevisionHistory from a dict
advisory_revision_history_from_dict = AdvisoryRevisionHistory.from_dict(advisory_revision_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


