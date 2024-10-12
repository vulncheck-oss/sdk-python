# AdvisoryRustsecFrontMatterAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | **List[str]** | Vulnerability aliases, e.g. CVE IDs (optional but recommended) Request a CVE for your RustSec vulns: https://iwantacve.org/ | [optional] 
**categories** | **List[str]** | Optional: Categories this advisory falls under. Valid categories are: \&quot;code-execution\&quot;, \&quot;crypto-failure\&quot;, \&quot;denial-of-service\&quot;, \&quot;file-disclosure\&quot; \&quot;format-injection\&quot;, \&quot;memory-corruption\&quot;, \&quot;memory-exposure\&quot;, \&quot;privilege-escalation\&quot; | [optional] 
**cvss** | **str** | Optional: a Common Vulnerability Scoring System score. More information can be found on the CVSS website, https://www.first.org/cvss/. | [optional] 
**var_date** | **str** | Disclosure date of the advisory as an RFC 3339 date (mandatory) | [optional] 
**informational** | **str** | Optional: Indicates the type of informational security  advisory  - \&quot;unsound\&quot; for soundness issues  - \&quot;unmaintained\&quot; for crates that are no longer maintained  - \&quot;notice\&quot; for other informational notices | [optional] 
**keywords** | **List[str]** | Freeform keywords which describe this vulnerability, similar to Cargo (optional) | [optional] 
**package** | **str** | Name of the affected crate (mandatory) | [optional] 
**references** | **List[str]** | URL to additional helpful references regarding the advisory (optional) | [optional] 
**related** | **List[str]** | Related vulnerabilities (optional) e.g. CVE for a C library wrapped by a -sys crate) | [optional] 
**rustsec_id** | **str** | Identifier for the advisory (mandatory). Will be assigned a \&quot;RUSTSEC-YYYY-NNNN\&quot; identifier e.g. RUSTSEC-2018-0001. Please use \&quot;RUSTSEC-0000-0000\&quot; in PRs. | [optional] 
**url** | **str** | URL to a long-form description of this issue, e.g. a GitHub issue/PR, a change log entry, or a blogpost announcing the release (optional) | [optional] 
**withdrawn** | **str** | Whether the advisory is withdrawn (optional) | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_rustsec_front_matter_advisory import AdvisoryRustsecFrontMatterAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRustsecFrontMatterAdvisory from a JSON string
advisory_rustsec_front_matter_advisory_instance = AdvisoryRustsecFrontMatterAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRustsecFrontMatterAdvisory.to_json())

# convert the object into a dict
advisory_rustsec_front_matter_advisory_dict = advisory_rustsec_front_matter_advisory_instance.to_dict()
# create an instance of AdvisoryRustsecFrontMatterAdvisory from a dict
advisory_rustsec_front_matter_advisory_from_dict = AdvisoryRustsecFrontMatterAdvisory.from_dict(advisory_rustsec_front_matter_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


