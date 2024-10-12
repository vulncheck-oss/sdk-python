# AdvisoryGreyNoiseDetection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**intention** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**recommend_block** | **bool** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**related_tags** | [**List[AdvisoryGreyNoiseTags]**](AdvisoryGreyNoiseTags.md) |  | [optional] 
**slug** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_grey_noise_detection import AdvisoryGreyNoiseDetection

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGreyNoiseDetection from a JSON string
advisory_grey_noise_detection_instance = AdvisoryGreyNoiseDetection.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGreyNoiseDetection.to_json())

# convert the object into a dict
advisory_grey_noise_detection_dict = advisory_grey_noise_detection_instance.to_dict()
# create an instance of AdvisoryGreyNoiseDetection from a dict
advisory_grey_noise_detection_from_dict = AdvisoryGreyNoiseDetection.from_dict(advisory_grey_noise_detection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


