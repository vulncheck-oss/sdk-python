# AdvisoryAffectedFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_last_modified** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_affected_file import AdvisoryAffectedFile

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAffectedFile from a JSON string
advisory_affected_file_instance = AdvisoryAffectedFile.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAffectedFile.to_json())

# convert the object into a dict
advisory_affected_file_dict = advisory_affected_file_instance.to_dict()
# create an instance of AdvisoryAffectedFile from a dict
advisory_affected_file_from_dict = AdvisoryAffectedFile.from_dict(advisory_affected_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


