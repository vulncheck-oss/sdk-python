# AdvisoryExodusIntel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**disclosed_public** | **str** |  | [optional] 
**disclosed_vendor** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_exodus_intel import AdvisoryExodusIntel

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryExodusIntel from a JSON string
advisory_exodus_intel_instance = AdvisoryExodusIntel.from_json(json)
# print the JSON string representation of the object
print(AdvisoryExodusIntel.to_json())

# convert the object into a dict
advisory_exodus_intel_dict = advisory_exodus_intel_instance.to_dict()
# create an instance of AdvisoryExodusIntel from a dict
advisory_exodus_intel_from_dict = AdvisoryExodusIntel.from_dict(advisory_exodus_intel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


