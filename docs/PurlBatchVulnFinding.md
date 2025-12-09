# PurlBatchVulnFinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cves** | **List[str]** | list of associated CVE &#39;s | [optional] 
**purl** | **str** | the purl, ex. hex/coherence@0.1.2 | [optional] 
**purl_struct** | [**PurlPackageURLJSON**](PurlPackageURLJSON.md) | meta-data about the purl | [optional] 
**research_attributes** | [**ApiOSSPackageResearchAttributes**](ApiOSSPackageResearchAttributes.md) |  | [optional] 
**vulnerabilities** | [**List[ApiOSSPackageVulnerability]**](ApiOSSPackageVulnerability.md) | list of associated vulnerabilities | [optional] 

## Example

```python
from vulncheck_sdk.models.purl_batch_vuln_finding import PurlBatchVulnFinding

# TODO update the JSON string below
json = "{}"
# create an instance of PurlBatchVulnFinding from a JSON string
purl_batch_vuln_finding_instance = PurlBatchVulnFinding.from_json(json)
# print the JSON string representation of the object
print(PurlBatchVulnFinding.to_json())

# convert the object into a dict
purl_batch_vuln_finding_dict = purl_batch_vuln_finding_instance.to_dict()
# create an instance of PurlBatchVulnFinding from a dict
purl_batch_vuln_finding_from_dict = PurlBatchVulnFinding.from_dict(purl_batch_vuln_finding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


