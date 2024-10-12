# AdvisoryFanuc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_fanuc import AdvisoryFanuc

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryFanuc from a JSON string
advisory_fanuc_instance = AdvisoryFanuc.from_json(json)
# print the JSON string representation of the object
print(AdvisoryFanuc.to_json())

# convert the object into a dict
advisory_fanuc_dict = advisory_fanuc_instance.to_dict()
# create an instance of AdvisoryFanuc from a dict
advisory_fanuc_from_dict = AdvisoryFanuc.from_dict(advisory_fanuc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


