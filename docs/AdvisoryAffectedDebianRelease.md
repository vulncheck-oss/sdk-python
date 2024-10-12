# AdvisoryAffectedDebianRelease


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixed_version** | **str** |  | [optional] 
**nodsa** | **str** |  | [optional] 
**nodsa_reason** | **str** |  | [optional] 
**release_name** | **str** |  | [optional] 
**repositories** | [**List[AdvisoryAffectedDebianRepository]**](AdvisoryAffectedDebianRepository.md) |  | [optional] 
**status** | **str** |  | [optional] 
**urgency** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_affected_debian_release import AdvisoryAffectedDebianRelease

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAffectedDebianRelease from a JSON string
advisory_affected_debian_release_instance = AdvisoryAffectedDebianRelease.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAffectedDebianRelease.to_json())

# convert the object into a dict
advisory_affected_debian_release_dict = advisory_affected_debian_release_instance.to_dict()
# create an instance of AdvisoryAffectedDebianRelease from a dict
advisory_affected_debian_release_from_dict = AdvisoryAffectedDebianRelease.from_dict(advisory_affected_debian_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


