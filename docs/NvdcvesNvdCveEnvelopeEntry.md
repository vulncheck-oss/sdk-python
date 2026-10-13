# NvdcvesNvdCveEnvelopeEntry

nvdcves.NvdCveEnvelopeEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | [**NvdcvesNvdCveExtended**](NvdcvesNvdCveExtended.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.nvdcves_nvd_cve_envelope_entry import NvdcvesNvdCveEnvelopeEntry

# TODO update the JSON string below
json = "{}"
# create an instance of NvdcvesNvdCveEnvelopeEntry from a JSON string
nvdcves_nvd_cve_envelope_entry_instance = NvdcvesNvdCveEnvelopeEntry.from_json(json)
# print the JSON string representation of the object
print(NvdcvesNvdCveEnvelopeEntry.to_json())

# convert the object into a dict
nvdcves_nvd_cve_envelope_entry_dict = nvdcves_nvd_cve_envelope_entry_instance.to_dict()
# create an instance of NvdcvesNvdCveEnvelopeEntry from a dict
nvdcves_nvd_cve_envelope_entry_from_dict = NvdcvesNvdCveEnvelopeEntry.from_dict(nvdcves_nvd_cve_envelope_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


