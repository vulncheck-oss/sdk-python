# AdvisoryYamaha


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **str** |  | [optional] 
**summary_ja** | **str** |  | [optional] 
**title_ja** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_yamaha import AdvisoryYamaha

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryYamaha from a JSON string
advisory_yamaha_instance = AdvisoryYamaha.from_json(json)
# print the JSON string representation of the object
print(AdvisoryYamaha.to_json())

# convert the object into a dict
advisory_yamaha_dict = advisory_yamaha_instance.to_dict()
# create an instance of AdvisoryYamaha from a dict
advisory_yamaha_from_dict = AdvisoryYamaha.from_dict(advisory_yamaha_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


