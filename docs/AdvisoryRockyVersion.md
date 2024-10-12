# AdvisoryRockyVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nvras** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_rocky_version import AdvisoryRockyVersion

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRockyVersion from a JSON string
advisory_rocky_version_instance = AdvisoryRockyVersion.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRockyVersion.to_json())

# convert the object into a dict
advisory_rocky_version_dict = advisory_rocky_version_instance.to_dict()
# create an instance of AdvisoryRockyVersion from a dict
advisory_rocky_version_from_dict = AdvisoryRockyVersion.from_dict(advisory_rocky_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


