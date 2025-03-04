# AdvisorySuseSecurity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_suse_security import AdvisorySuseSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySuseSecurity from a JSON string
advisory_suse_security_instance = AdvisorySuseSecurity.from_json(json)
# print the JSON string representation of the object
print(AdvisorySuseSecurity.to_json())

# convert the object into a dict
advisory_suse_security_dict = advisory_suse_security_instance.to_dict()
# create an instance of AdvisorySuseSecurity from a dict
advisory_suse_security_from_dict = AdvisorySuseSecurity.from_dict(advisory_suse_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


