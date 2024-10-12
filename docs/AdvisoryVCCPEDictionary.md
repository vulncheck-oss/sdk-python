# AdvisoryVCCPEDictionary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_cpe** | **str** |  | [optional] 
**versions** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_vccpe_dictionary import AdvisoryVCCPEDictionary

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVCCPEDictionary from a JSON string
advisory_vccpe_dictionary_instance = AdvisoryVCCPEDictionary.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVCCPEDictionary.to_json())

# convert the object into a dict
advisory_vccpe_dictionary_dict = advisory_vccpe_dictionary_instance.to_dict()
# create an instance of AdvisoryVCCPEDictionary from a dict
advisory_vccpe_dictionary_from_dict = AdvisoryVCCPEDictionary.from_dict(advisory_vccpe_dictionary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


