# AdvisoryCertIRSecurityAlert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary_fa** | **str** |  | [optional] 
**title_fa** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cert_ir_security_alert import AdvisoryCertIRSecurityAlert

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCertIRSecurityAlert from a JSON string
advisory_cert_ir_security_alert_instance = AdvisoryCertIRSecurityAlert.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCertIRSecurityAlert.to_json())

# convert the object into a dict
advisory_cert_ir_security_alert_dict = advisory_cert_ir_security_alert_instance.to_dict()
# create an instance of AdvisoryCertIRSecurityAlert from a dict
advisory_cert_ir_security_alert_from_dict = AdvisoryCertIRSecurityAlert.from_dict(advisory_cert_ir_security_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


