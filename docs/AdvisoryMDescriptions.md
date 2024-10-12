# AdvisoryMDescriptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lang** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_m_descriptions import AdvisoryMDescriptions

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMDescriptions from a JSON string
advisory_m_descriptions_instance = AdvisoryMDescriptions.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMDescriptions.to_json())

# convert the object into a dict
advisory_m_descriptions_dict = advisory_m_descriptions_instance.to_dict()
# create an instance of AdvisoryMDescriptions from a dict
advisory_m_descriptions_from_dict = AdvisoryMDescriptions.from_dict(advisory_m_descriptions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


