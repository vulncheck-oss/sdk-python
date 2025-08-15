# AdvisoryGMOCyberSecurity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary_ja** | **str** |  | [optional] 
**title_ja** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_gmo_cyber_security import AdvisoryGMOCyberSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGMOCyberSecurity from a JSON string
advisory_gmo_cyber_security_instance = AdvisoryGMOCyberSecurity.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGMOCyberSecurity.to_json())

# convert the object into a dict
advisory_gmo_cyber_security_dict = advisory_gmo_cyber_security_instance.to_dict()
# create an instance of AdvisoryGMOCyberSecurity from a dict
advisory_gmo_cyber_security_from_dict = AdvisoryGMOCyberSecurity.from_dict(advisory_gmo_cyber_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


