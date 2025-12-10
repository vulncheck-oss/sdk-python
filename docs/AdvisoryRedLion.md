# AdvisoryRedLion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_red_lion import AdvisoryRedLion

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRedLion from a JSON string
advisory_red_lion_instance = AdvisoryRedLion.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRedLion.to_json())

# convert the object into a dict
advisory_red_lion_dict = advisory_red_lion_instance.to_dict()
# create an instance of AdvisoryRedLion from a dict
advisory_red_lion_from_dict = AdvisoryRedLion.from_dict(advisory_red_lion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


