# AdvisorySiemensRevisionHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**legacy_version** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_siemens_revision_history import AdvisorySiemensRevisionHistory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySiemensRevisionHistory from a JSON string
advisory_siemens_revision_history_instance = AdvisorySiemensRevisionHistory.from_json(json)
# print the JSON string representation of the object
print(AdvisorySiemensRevisionHistory.to_json())

# convert the object into a dict
advisory_siemens_revision_history_dict = advisory_siemens_revision_history_instance.to_dict()
# create an instance of AdvisorySiemensRevisionHistory from a dict
advisory_siemens_revision_history_from_dict = AdvisorySiemensRevisionHistory.from_dict(advisory_siemens_revision_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


