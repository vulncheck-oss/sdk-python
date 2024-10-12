# AdvisoryDebianSecurityAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_packages** | [**List[AdvisoryAffectedDebianPackage]**](AdvisoryAffectedDebianPackage.md) |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**dsa** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_debian_security_advisory import AdvisoryDebianSecurityAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryDebianSecurityAdvisory from a JSON string
advisory_debian_security_advisory_instance = AdvisoryDebianSecurityAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryDebianSecurityAdvisory.to_json())

# convert the object into a dict
advisory_debian_security_advisory_dict = advisory_debian_security_advisory_instance.to_dict()
# create an instance of AdvisoryDebianSecurityAdvisory from a dict
advisory_debian_security_advisory_from_dict = AdvisoryDebianSecurityAdvisory.from_dict(advisory_debian_security_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


