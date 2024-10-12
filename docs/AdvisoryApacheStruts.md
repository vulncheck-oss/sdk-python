# AdvisoryApacheStruts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**impact** | **str** |  | [optional] 
**rating** | **str** |  | [optional] 
**remediation** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vulnerable_version** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_apache_struts import AdvisoryApacheStruts

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryApacheStruts from a JSON string
advisory_apache_struts_instance = AdvisoryApacheStruts.from_json(json)
# print the JSON string representation of the object
print(AdvisoryApacheStruts.to_json())

# convert the object into a dict
advisory_apache_struts_dict = advisory_apache_struts_instance.to_dict()
# create an instance of AdvisoryApacheStruts from a dict
advisory_apache_struts_from_dict = AdvisoryApacheStruts.from_dict(advisory_apache_struts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


