# AdvisorySecurityLab


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**title_ru** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_security_lab import AdvisorySecurityLab

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySecurityLab from a JSON string
advisory_security_lab_instance = AdvisorySecurityLab.from_json(json)
# print the JSON string representation of the object
print(AdvisorySecurityLab.to_json())

# convert the object into a dict
advisory_security_lab_dict = advisory_security_lab_instance.to_dict()
# create an instance of AdvisorySecurityLab from a dict
advisory_security_lab_from_dict = AdvisorySecurityLab.from_dict(advisory_security_lab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


