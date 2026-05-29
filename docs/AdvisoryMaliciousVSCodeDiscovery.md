# AdvisoryMaliciousVSCodeDiscovery

advisory.MaliciousVSCodeDiscovery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Date the timestamp when the discovery was published (via the \&quot;reference\&quot;) | [optional] 
**marketplace** | **List[str]** | Marketplace list of names of the marketplaces where the extension versions are available | [optional] 
**reference** | **str** | Reference location where the initial public release of the vulnerability was pulled | [optional] 
**type** | **str** | Type VulnCheck vulnerability classification | [optional] 
**versions** | **List[str]** | Versions list of vulnerable versions | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_malicious_vs_code_discovery import AdvisoryMaliciousVSCodeDiscovery

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMaliciousVSCodeDiscovery from a JSON string
advisory_malicious_vs_code_discovery_instance = AdvisoryMaliciousVSCodeDiscovery.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMaliciousVSCodeDiscovery.to_json())

# convert the object into a dict
advisory_malicious_vs_code_discovery_dict = advisory_malicious_vs_code_discovery_instance.to_dict()
# create an instance of AdvisoryMaliciousVSCodeDiscovery from a dict
advisory_malicious_vs_code_discovery_from_dict = AdvisoryMaliciousVSCodeDiscovery.from_dict(advisory_malicious_vs_code_discovery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


