# AdvisoryRRevision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**description** | [**AdvisoryRDescription**](AdvisoryRDescription.md) |  | [optional] 
**number** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_r_revision import AdvisoryRRevision

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRRevision from a JSON string
advisory_r_revision_instance = AdvisoryRRevision.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRRevision.to_json())

# convert the object into a dict
advisory_r_revision_dict = advisory_r_revision_instance.to_dict()
# create an instance of AdvisoryRRevision from a dict
advisory_r_revision_from_dict = AdvisoryRRevision.from_dict(advisory_r_revision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


