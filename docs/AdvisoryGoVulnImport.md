# AdvisoryGoVulnImport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional] 
**symbols** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_go_vuln_import import AdvisoryGoVulnImport

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGoVulnImport from a JSON string
advisory_go_vuln_import_instance = AdvisoryGoVulnImport.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGoVulnImport.to_json())

# convert the object into a dict
advisory_go_vuln_import_dict = advisory_go_vuln_import_instance.to_dict()
# create an instance of AdvisoryGoVulnImport from a dict
advisory_go_vuln_import_from_dict = AdvisoryGoVulnImport.from_dict(advisory_go_vuln_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


