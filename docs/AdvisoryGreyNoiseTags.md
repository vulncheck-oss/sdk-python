# AdvisoryGreyNoiseTags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**intention** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**slug** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_grey_noise_tags import AdvisoryGreyNoiseTags

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGreyNoiseTags from a JSON string
advisory_grey_noise_tags_instance = AdvisoryGreyNoiseTags.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGreyNoiseTags.to_json())

# convert the object into a dict
advisory_grey_noise_tags_dict = advisory_grey_noise_tags_instance.to_dict()
# create an instance of AdvisoryGreyNoiseTags from a dict
advisory_grey_noise_tags_from_dict = AdvisoryGreyNoiseTags.from_dict(advisory_grey_noise_tags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


