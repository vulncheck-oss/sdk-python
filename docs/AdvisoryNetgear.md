# AdvisoryNetgear


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**products** | **List[str]** |  | [optional] 
**psvn_number** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_netgear import AdvisoryNetgear

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNetgear from a JSON string
advisory_netgear_instance = AdvisoryNetgear.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNetgear.to_json())

# convert the object into a dict
advisory_netgear_dict = advisory_netgear_instance.to_dict()
# create an instance of AdvisoryNetgear from a dict
advisory_netgear_from_dict = AdvisoryNetgear.from_dict(advisory_netgear_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


