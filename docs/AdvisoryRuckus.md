# AdvisoryRuckus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ruckus import AdvisoryRuckus

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRuckus from a JSON string
advisory_ruckus_instance = AdvisoryRuckus.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRuckus.to_json())

# convert the object into a dict
advisory_ruckus_dict = advisory_ruckus_instance.to_dict()
# create an instance of AdvisoryRuckus from a dict
advisory_ruckus_from_dict = AdvisoryRuckus.from_dict(advisory_ruckus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


