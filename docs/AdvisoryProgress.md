# AdvisoryProgress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_progress import AdvisoryProgress

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryProgress from a JSON string
advisory_progress_instance = AdvisoryProgress.from_json(json)
# print the JSON string representation of the object
print(AdvisoryProgress.to_json())

# convert the object into a dict
advisory_progress_dict = advisory_progress_instance.to_dict()
# create an instance of AdvisoryProgress from a dict
advisory_progress_from_dict = AdvisoryProgress.from_dict(advisory_progress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


