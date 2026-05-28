# AdvisoryVersionChange

advisory.VersionChange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_version_change import AdvisoryVersionChange

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVersionChange from a JSON string
advisory_version_change_instance = AdvisoryVersionChange.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVersionChange.to_json())

# convert the object into a dict
advisory_version_change_dict = advisory_version_change_instance.to_dict()
# create an instance of AdvisoryVersionChange from a dict
advisory_version_change_from_dict = AdvisoryVersionChange.from_dict(advisory_version_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


