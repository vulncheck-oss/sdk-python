# AdvisoryVulnCheckCVEListV5


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**mitre_ref** | [**AdvisoryMitreCVEListV5Ref**](AdvisoryMitreCVEListV5Ref.md) |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_vuln_check_cve_list_v5 import AdvisoryVulnCheckCVEListV5

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVulnCheckCVEListV5 from a JSON string
advisory_vuln_check_cve_list_v5_instance = AdvisoryVulnCheckCVEListV5.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVulnCheckCVEListV5.to_json())

# convert the object into a dict
advisory_vuln_check_cve_list_v5_dict = advisory_vuln_check_cve_list_v5_instance.to_dict()
# create an instance of AdvisoryVulnCheckCVEListV5 from a dict
advisory_vuln_check_cve_list_v5_from_dict = AdvisoryVulnCheckCVEListV5.from_dict(advisory_vuln_check_cve_list_v5_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


