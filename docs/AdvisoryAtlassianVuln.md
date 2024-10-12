# AdvisoryAtlassianVuln


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**products** | [**List[AdvisoryAtlassianProducts]**](AdvisoryAtlassianProducts.md) |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_atlassian_vuln import AdvisoryAtlassianVuln

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAtlassianVuln from a JSON string
advisory_atlassian_vuln_instance = AdvisoryAtlassianVuln.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAtlassianVuln.to_json())

# convert the object into a dict
advisory_atlassian_vuln_dict = advisory_atlassian_vuln_instance.to_dict()
# create an instance of AdvisoryAtlassianVuln from a dict
advisory_atlassian_vuln_from_dict = AdvisoryAtlassianVuln.from_dict(advisory_atlassian_vuln_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


