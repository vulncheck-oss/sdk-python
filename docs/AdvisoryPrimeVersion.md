# AdvisoryPrimeVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jd_k** | **str** |  | [optional] 
**prime** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_prime_version import AdvisoryPrimeVersion

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPrimeVersion from a JSON string
advisory_prime_version_instance = AdvisoryPrimeVersion.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPrimeVersion.to_json())

# convert the object into a dict
advisory_prime_version_dict = advisory_prime_version_instance.to_dict()
# create an instance of AdvisoryPrimeVersion from a dict
advisory_prime_version_from_dict = AdvisoryPrimeVersion.from_dict(advisory_prime_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


