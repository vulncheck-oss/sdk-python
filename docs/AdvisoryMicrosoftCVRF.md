# AdvisoryMicrosoftCVRF


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**cvrf** | [**AdvisoryMSCVRF**](AdvisoryMSCVRF.md) |  | [optional] 
**date_added** | **str** |  | [optional] 
**exploited_list** | [**List[AdvisoryITW]**](AdvisoryITW.md) |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_microsoft_cvrf import AdvisoryMicrosoftCVRF

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMicrosoftCVRF from a JSON string
advisory_microsoft_cvrf_instance = AdvisoryMicrosoftCVRF.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMicrosoftCVRF.to_json())

# convert the object into a dict
advisory_microsoft_cvrf_dict = advisory_microsoft_cvrf_instance.to_dict()
# create an instance of AdvisoryMicrosoftCVRF from a dict
advisory_microsoft_cvrf_from_dict = AdvisoryMicrosoftCVRF.from_dict(advisory_microsoft_cvrf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


