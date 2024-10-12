# AdvisoryOmron


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
from vulncheck_sdk.models.advisory_omron import AdvisoryOmron

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOmron from a JSON string
advisory_omron_instance = AdvisoryOmron.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOmron.to_json())

# convert the object into a dict
advisory_omron_dict = advisory_omron_instance.to_dict()
# create an instance of AdvisoryOmron from a dict
advisory_omron_from_dict = AdvisoryOmron.from_dict(advisory_omron_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


