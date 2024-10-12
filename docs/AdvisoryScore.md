# AdvisoryScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **str** |  | [optional] 
**in_kev** | **bool** |  | [optional] 
**in_vckev** | **bool** |  | [optional] 
**reference_urls** | [**List[AdvisoryRefURL]**](AdvisoryRefURL.md) |  | [optional] 
**score** | **int** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_score import AdvisoryScore

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryScore from a JSON string
advisory_score_instance = AdvisoryScore.from_json(json)
# print the JSON string representation of the object
print(AdvisoryScore.to_json())

# convert the object into a dict
advisory_score_dict = advisory_score_instance.to_dict()
# create an instance of AdvisoryScore from a dict
advisory_score_from_dict = AdvisoryScore.from_dict(advisory_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


