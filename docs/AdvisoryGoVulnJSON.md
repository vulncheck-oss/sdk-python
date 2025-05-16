# AdvisoryGoVulnJSON


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory_url** | **str** |  | [optional] 
**affected** | [**List[AdvisoryGoVulnAffected]**](AdvisoryGoVulnAffected.md) |  | [optional] 
**aliases** | **List[str]** |  | [optional] 
**credits** | [**List[AdvisoryGoCredits]**](AdvisoryGoCredits.md) |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**details** | **str** |  | [optional] 
**ghsa** | **List[str]** |  | [optional] 
**go_advisory_id** | **str** |  | [optional] 
**modified** | **str** |  | [optional] 
**published** | **str** |  | [optional] 
**references** | [**List[AdvisoryGoVulnReference]**](AdvisoryGoVulnReference.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_go_vuln_json import AdvisoryGoVulnJSON

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGoVulnJSON from a JSON string
advisory_go_vuln_json_instance = AdvisoryGoVulnJSON.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGoVulnJSON.to_json())

# convert the object into a dict
advisory_go_vuln_json_dict = advisory_go_vuln_json_instance.to_dict()
# create an instance of AdvisoryGoVulnJSON from a dict
advisory_go_vuln_json_from_dict = AdvisoryGoVulnJSON.from_dict(advisory_go_vuln_json_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


