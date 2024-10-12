# ApiReferencesExtended


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_data** | [**List[ApiReferenceDataExtended]**](ApiReferenceDataExtended.md) | ExploitData     []NormalizedExploit       &#x60;json:\&quot;exploit_data,omitempty\&quot;&#x60;   ThreatActorData []ThreatActorExtended     &#x60;json:\&quot;threat_actor_data,omitempty\&quot;&#x60;   RansomwareData  []RansomwareReferenceData &#x60;json:\&quot;ransomware_data,omitempty\&quot;&#x60;   AdvisoryData    []AdvisoryExtended        &#x60;json:\&quot;advisory_data,omitempty\&quot;&#x60;   IdentifierData  []IdentifierExtended      &#x60;json:\&quot;identifier_data,omitempty\&quot;&#x60; | [optional] 

## Example

```python
from vulncheck_sdk.models.api_references_extended import ApiReferencesExtended

# TODO update the JSON string below
json = "{}"
# create an instance of ApiReferencesExtended from a JSON string
api_references_extended_instance = ApiReferencesExtended.from_json(json)
# print the JSON string representation of the object
print(ApiReferencesExtended.to_json())

# convert the object into a dict
api_references_extended_dict = api_references_extended_instance.to_dict()
# create an instance of ApiReferencesExtended from a dict
api_references_extended_from_dict = ApiReferencesExtended.from_dict(api_references_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


