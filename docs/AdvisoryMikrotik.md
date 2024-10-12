# AdvisoryMikrotik


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_mikrotik import AdvisoryMikrotik

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMikrotik from a JSON string
advisory_mikrotik_instance = AdvisoryMikrotik.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMikrotik.to_json())

# convert the object into a dict
advisory_mikrotik_dict = advisory_mikrotik_instance.to_dict()
# create an instance of AdvisoryMikrotik from a dict
advisory_mikrotik_from_dict = AdvisoryMikrotik.from_dict(advisory_mikrotik_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


