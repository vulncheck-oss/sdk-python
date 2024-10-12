# AdvisoryCompassSecurity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csnc_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**effect** | **str** |  | [optional] 
**introduction** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**risk** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_compass_security import AdvisoryCompassSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCompassSecurity from a JSON string
advisory_compass_security_instance = AdvisoryCompassSecurity.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCompassSecurity.to_json())

# convert the object into a dict
advisory_compass_security_dict = advisory_compass_security_instance.to_dict()
# create an instance of AdvisoryCompassSecurity from a dict
advisory_compass_security_from_dict = AdvisoryCompassSecurity.from_dict(advisory_compass_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


