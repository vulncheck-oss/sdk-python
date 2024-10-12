# AdvisoryMIdentification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | [**AdvisoryIVal**](AdvisoryIVal.md) |  | [optional] 
**id** | [**AdvisoryIVal**](AdvisoryIVal.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_m_identification import AdvisoryMIdentification

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMIdentification from a JSON string
advisory_m_identification_instance = AdvisoryMIdentification.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMIdentification.to_json())

# convert the object into a dict
advisory_m_identification_dict = advisory_m_identification_instance.to_dict()
# create an instance of AdvisoryMIdentification from a dict
advisory_m_identification_from_dict = AdvisoryMIdentification.from_dict(advisory_m_identification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


