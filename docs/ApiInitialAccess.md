# ApiInitialAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifacts** | [**List[ApiInitialAccessArtifact]**](ApiInitialAccessArtifact.md) | Artifacts holds the set of available artifacts for this vulnerability, such as exploit, shodan queries, PCAP traces, and others. | [optional] 
**cve** | **str** | CVE identifier for the given initial access record. | [optional] 
**in_kev** | **bool** | InKEV is true if this artifact is in CISA&#39;s Known Exploited Vulnerabilities (KEV) data set; otherwise, false. | [optional] 
**in_vckev** | **bool** | InVCKEV is true if this artifact is in VulnCheck&#39;s Known Exploited Vulnerabilities (VCKEV) data set; otherwise, false. | [optional] 
**vulnerable_cpes** | **List[str]** | VulnerableCPEs is the list of vulnerable CPE strings associated with this CVE and artifact(s). | [optional] 

## Example

```python
from vulncheck_sdk.models.api_initial_access import ApiInitialAccess

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInitialAccess from a JSON string
api_initial_access_instance = ApiInitialAccess.from_json(json)
# print the JSON string representation of the object
print(ApiInitialAccess.to_json())

# convert the object into a dict
api_initial_access_dict = api_initial_access_instance.to_dict()
# create an instance of ApiInitialAccess from a dict
api_initial_access_from_dict = ApiInitialAccess.from_dict(api_initial_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


