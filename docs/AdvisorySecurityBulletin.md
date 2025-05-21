# AdvisorySecurityBulletin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acknowledgement** | **str** |  | [optional] 
**bulletin_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvedetails** | [**List[AdvisoryCVEDetail]**](AdvisoryCVEDetail.md) |  | [optional] 
**date_added** | **str** |  | [optional] 
**hardware_updates** | [**List[AdvisoryHardwareUpdate]**](AdvisoryHardwareUpdate.md) |  | [optional] 
**last_updated** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**revisions** | [**List[AdvisoryNvidiaRevision]**](AdvisoryNvidiaRevision.md) |  | [optional] 
**severity** | **str** |  | [optional] 
**software_updates** | [**List[AdvisorySoftwareUpdate]**](AdvisorySoftwareUpdate.md) |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_security_bulletin import AdvisorySecurityBulletin

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySecurityBulletin from a JSON string
advisory_security_bulletin_instance = AdvisorySecurityBulletin.from_json(json)
# print the JSON string representation of the object
print(AdvisorySecurityBulletin.to_json())

# convert the object into a dict
advisory_security_bulletin_dict = advisory_security_bulletin_instance.to_dict()
# create an instance of AdvisorySecurityBulletin from a dict
advisory_security_bulletin_from_dict = AdvisorySecurityBulletin.from_dict(advisory_security_bulletin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


