# AdvisoryCorrection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**corrected_at** | **str** |  | [optional] 
**orelease** | **str** |  | [optional] 
**release** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_correction import AdvisoryCorrection

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCorrection from a JSON string
advisory_correction_instance = AdvisoryCorrection.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCorrection.to_json())

# convert the object into a dict
advisory_correction_dict = advisory_correction_instance.to_dict()
# create an instance of AdvisoryCorrection from a dict
advisory_correction_from_dict = AdvisoryCorrection.from_dict(advisory_correction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


