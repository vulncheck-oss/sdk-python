# AdvisoryAndroidAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | [**List[AdvisoryAndroidAffected]**](AdvisoryAndroidAffected.md) |  | [optional] 
**aliases** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**modified** | **str** |  | [optional] 
**published** | **str** |  | [optional] 
**references** | [**List[AdvisoryAndroidReference]**](AdvisoryAndroidReference.md) |  | [optional] 
**summary** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_android_advisory import AdvisoryAndroidAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAndroidAdvisory from a JSON string
advisory_android_advisory_instance = AdvisoryAndroidAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAndroidAdvisory.to_json())

# convert the object into a dict
advisory_android_advisory_dict = advisory_android_advisory_instance.to_dict()
# create an instance of AdvisoryAndroidAdvisory from a dict
advisory_android_advisory_from_dict = AdvisoryAndroidAdvisory.from_dict(advisory_android_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


