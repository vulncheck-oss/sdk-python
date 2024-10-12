# AdvisoryNodeSecurity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_environments** | **List[str]** |  | [optional] 
**author** | [**AdvisoryNodeAuthor**](AdvisoryNodeAuthor.md) |  | [optional] 
**coordinating_vendor** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss_score** | **float** |  | [optional] 
**cvss_vector** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**module_name** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**patched_versions** | **str** |  | [optional] 
**publish_date** | **str** |  | [optional] 
**recommendation** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vulnerable_versions** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_node_security import AdvisoryNodeSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNodeSecurity from a JSON string
advisory_node_security_instance = AdvisoryNodeSecurity.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNodeSecurity.to_json())

# convert the object into a dict
advisory_node_security_dict = advisory_node_security_instance.to_dict()
# create an instance of AdvisoryNodeSecurity from a dict
advisory_node_security_from_dict = AdvisoryNodeSecurity.from_dict(advisory_node_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


