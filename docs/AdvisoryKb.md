# AdvisoryKb


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kb_url** | **str** |  | [optional] 
**ms_date_added** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**supercedence** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_kb import AdvisoryKb

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryKb from a JSON string
advisory_kb_instance = AdvisoryKb.from_json(json)
# print the JSON string representation of the object
print(AdvisoryKb.to_json())

# convert the object into a dict
advisory_kb_dict = advisory_kb_instance.to_dict()
# create an instance of AdvisoryKb from a dict
advisory_kb_from_dict = AdvisoryKb.from_dict(advisory_kb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


