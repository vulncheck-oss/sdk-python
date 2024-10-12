# AdvisorySiemensGenerator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**engine** | [**AdvisorySiemensEngine**](AdvisorySiemensEngine.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_siemens_generator import AdvisorySiemensGenerator

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySiemensGenerator from a JSON string
advisory_siemens_generator_instance = AdvisorySiemensGenerator.from_json(json)
# print the JSON string representation of the object
print(AdvisorySiemensGenerator.to_json())

# convert the object into a dict
advisory_siemens_generator_dict = advisory_siemens_generator_instance.to_dict()
# create an instance of AdvisorySiemensGenerator from a dict
advisory_siemens_generator_from_dict = AdvisorySiemensGenerator.from_dict(advisory_siemens_generator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


