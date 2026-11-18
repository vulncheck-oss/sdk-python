# RestNvdChangeEnvelopeEntry

rest.NvdChangeEnvelopeEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change** | [**RestNvdChange**](RestNvdChange.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.rest_nvd_change_envelope_entry import RestNvdChangeEnvelopeEntry

# TODO update the JSON string below
json = "{}"
# create an instance of RestNvdChangeEnvelopeEntry from a JSON string
rest_nvd_change_envelope_entry_instance = RestNvdChangeEnvelopeEntry.from_json(json)
# print the JSON string representation of the object
print(RestNvdChangeEnvelopeEntry.to_json())

# convert the object into a dict
rest_nvd_change_envelope_entry_dict = rest_nvd_change_envelope_entry_instance.to_dict()
# create an instance of RestNvdChangeEnvelopeEntry from a dict
rest_nvd_change_envelope_entry_from_dict = RestNvdChangeEnvelopeEntry.from_dict(rest_nvd_change_envelope_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


