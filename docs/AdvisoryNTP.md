# AdvisoryNTP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **List[str]** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ntp import AdvisoryNTP

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNTP from a JSON string
advisory_ntp_instance = AdvisoryNTP.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNTP.to_json())

# convert the object into a dict
advisory_ntp_dict = advisory_ntp_instance.to_dict()
# create an instance of AdvisoryNTP from a dict
advisory_ntp_from_dict = AdvisoryNTP.from_dict(advisory_ntp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


