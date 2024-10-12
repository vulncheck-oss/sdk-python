# AdvisoryAndroidAffected


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ecosystem_specific** | [**AdvisoryEcoSystem**](AdvisoryEcoSystem.md) |  | [optional] 
**package** | [**AdvisoryAndroidPackage**](AdvisoryAndroidPackage.md) |  | [optional] 
**ranges** | [**List[AdvisoryAndroidRange]**](AdvisoryAndroidRange.md) |  | [optional] 
**versions** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_android_affected import AdvisoryAndroidAffected

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAndroidAffected from a JSON string
advisory_android_affected_instance = AdvisoryAndroidAffected.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAndroidAffected.to_json())

# convert the object into a dict
advisory_android_affected_dict = advisory_android_affected_instance.to_dict()
# create an instance of AdvisoryAndroidAffected from a dict
advisory_android_affected_from_dict = AdvisoryAndroidAffected.from_dict(advisory_android_affected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


