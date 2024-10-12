# AdvisoryAndroidReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_android_reference import AdvisoryAndroidReference

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAndroidReference from a JSON string
advisory_android_reference_instance = AdvisoryAndroidReference.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAndroidReference.to_json())

# convert the object into a dict
advisory_android_reference_dict = advisory_android_reference_instance.to_dict()
# create an instance of AdvisoryAndroidReference from a dict
advisory_android_reference_from_dict = AdvisoryAndroidReference.from_dict(advisory_android_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


