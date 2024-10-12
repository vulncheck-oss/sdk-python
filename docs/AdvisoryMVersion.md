# AdvisoryMVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**less_than** | **str** |  | [optional] 
**less_than_or_equal** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**version_type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_m_version import AdvisoryMVersion

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMVersion from a JSON string
advisory_m_version_instance = AdvisoryMVersion.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMVersion.to_json())

# convert the object into a dict
advisory_m_version_dict = advisory_m_version_instance.to_dict()
# create an instance of AdvisoryMVersion from a dict
advisory_m_version_from_dict = AdvisoryMVersion.from_dict(advisory_m_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


