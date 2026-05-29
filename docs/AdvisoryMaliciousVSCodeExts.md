# AdvisoryMaliciousVSCodeExts

advisory.MaliciousVSCodeExts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discoveries** | [**List[AdvisoryMaliciousVSCodeDiscovery]**](AdvisoryMaliciousVSCodeDiscovery.md) | Discoveries list of individual vulnerability reports, sorted chronologically by discovery date | [optional] 
**first_seen** | **str** | FirstSeen the earliest date the vulnerability was observed or created in our system | [optional] 
**last_updated** | **str** | LastUpdated the most recent date when any discovery was added for this extension | [optional] 
**marketplace** | **List[str]** | Marketplace list of names of the marketplaces where the extension versions are available | [optional] 
**name** | **str** | Name is the name of the extension | [optional] 
**publisher** | **str** | Publisher name of the publisher of the extension | [optional] 
**references** | **List[str]** | Reference list of locations where the public releases about the vulnerabilities were pulled | [optional] 
**types** | **List[str]** | Types VulnCheck vulnerability classifications found for this extension | [optional] 
**versions** | **List[str]** | Versions list of vulnerable versions | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_malicious_vs_code_exts import AdvisoryMaliciousVSCodeExts

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMaliciousVSCodeExts from a JSON string
advisory_malicious_vs_code_exts_instance = AdvisoryMaliciousVSCodeExts.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMaliciousVSCodeExts.to_json())

# convert the object into a dict
advisory_malicious_vs_code_exts_dict = advisory_malicious_vs_code_exts_instance.to_dict()
# create an instance of AdvisoryMaliciousVSCodeExts from a dict
advisory_malicious_vs_code_exts_from_dict = AdvisoryMaliciousVSCodeExts.from_dict(advisory_malicious_vs_code_exts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


