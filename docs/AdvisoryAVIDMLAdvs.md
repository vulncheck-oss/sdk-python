# AdvisoryAVIDMLAdvs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_avidml_advs import AdvisoryAVIDMLAdvs

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAVIDMLAdvs from a JSON string
advisory_avidml_advs_instance = AdvisoryAVIDMLAdvs.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAVIDMLAdvs.to_json())

# convert the object into a dict
advisory_avidml_advs_dict = advisory_avidml_advs_instance.to_dict()
# create an instance of AdvisoryAVIDMLAdvs from a dict
advisory_avidml_advs_from_dict = AdvisoryAVIDMLAdvs.from_dict(advisory_avidml_advs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


