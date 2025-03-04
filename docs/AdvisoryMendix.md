# AdvisoryMendix


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **List[str]** |  | [optional] 
**id** | **str** |  | [optional] 
**mendix_id** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_mendix import AdvisoryMendix

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMendix from a JSON string
advisory_mendix_instance = AdvisoryMendix.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMendix.to_json())

# convert the object into a dict
advisory_mendix_dict = advisory_mendix_instance.to_dict()
# create an instance of AdvisoryMendix from a dict
advisory_mendix_from_dict = AdvisoryMendix.from_dict(advisory_mendix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


