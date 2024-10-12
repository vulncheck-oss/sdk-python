# AdvisoryFlattSecurity


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
from vulncheck_sdk.models.advisory_flatt_security import AdvisoryFlattSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryFlattSecurity from a JSON string
advisory_flatt_security_instance = AdvisoryFlattSecurity.from_json(json)
# print the JSON string representation of the object
print(AdvisoryFlattSecurity.to_json())

# convert the object into a dict
advisory_flatt_security_dict = advisory_flatt_security_instance.to_dict()
# create an instance of AdvisoryFlattSecurity from a dict
advisory_flatt_security_from_dict = AdvisoryFlattSecurity.from_dict(advisory_flatt_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


