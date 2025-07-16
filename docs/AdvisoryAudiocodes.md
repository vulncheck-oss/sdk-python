# AdvisoryAudiocodes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_audiocodes import AdvisoryAudiocodes

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAudiocodes from a JSON string
advisory_audiocodes_instance = AdvisoryAudiocodes.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAudiocodes.to_json())

# convert the object into a dict
advisory_audiocodes_dict = advisory_audiocodes_instance.to_dict()
# create an instance of AdvisoryAudiocodes from a dict
advisory_audiocodes_from_dict = AdvisoryAudiocodes.from_dict(advisory_audiocodes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


