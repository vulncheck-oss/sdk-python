# AdvisoryZuluVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jdk** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**zulu** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_zulu_version import AdvisoryZuluVersion

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryZuluVersion from a JSON string
advisory_zulu_version_instance = AdvisoryZuluVersion.from_json(json)
# print the JSON string representation of the object
print(AdvisoryZuluVersion.to_json())

# convert the object into a dict
advisory_zulu_version_dict = advisory_zulu_version_instance.to_dict()
# create an instance of AdvisoryZuluVersion from a dict
advisory_zulu_version_from_dict = AdvisoryZuluVersion.from_dict(advisory_zulu_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


