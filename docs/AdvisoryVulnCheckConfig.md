# AdvisoryVulnCheckConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**List[AdvisoryNVD20Configuration]**](AdvisoryNVD20Configuration.md) |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_vuln_check_config import AdvisoryVulnCheckConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVulnCheckConfig from a JSON string
advisory_vuln_check_config_instance = AdvisoryVulnCheckConfig.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVulnCheckConfig.to_json())

# convert the object into a dict
advisory_vuln_check_config_dict = advisory_vuln_check_config_instance.to_dict()
# create an instance of AdvisoryVulnCheckConfig from a dict
advisory_vuln_check_config_from_dict = AdvisoryVulnCheckConfig.from_dict(advisory_vuln_check_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


