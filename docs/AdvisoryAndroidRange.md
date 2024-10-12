# AdvisoryAndroidRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[AdvisoryAndroidEvent]**](AdvisoryAndroidEvent.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_android_range import AdvisoryAndroidRange

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAndroidRange from a JSON string
advisory_android_range_instance = AdvisoryAndroidRange.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAndroidRange.to_json())

# convert the object into a dict
advisory_android_range_dict = advisory_android_range_instance.to_dict()
# create an instance of AdvisoryAndroidRange from a dict
advisory_android_range_from_dict = AdvisoryAndroidRange.from_dict(advisory_android_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


