# AdvisoryAffectedDebianRepository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_affected_debian_repository import AdvisoryAffectedDebianRepository

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAffectedDebianRepository from a JSON string
advisory_affected_debian_repository_instance = AdvisoryAffectedDebianRepository.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAffectedDebianRepository.to_json())

# convert the object into a dict
advisory_affected_debian_repository_dict = advisory_affected_debian_repository_instance.to_dict()
# create an instance of AdvisoryAffectedDebianRepository from a dict
advisory_affected_debian_repository_from_dict = AdvisoryAffectedDebianRepository.from_dict(advisory_affected_debian_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


