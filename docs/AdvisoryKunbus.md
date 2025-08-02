# AdvisoryKunbus


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
from vulncheck_sdk.models.advisory_kunbus import AdvisoryKunbus

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryKunbus from a JSON string
advisory_kunbus_instance = AdvisoryKunbus.from_json(json)
# print the JSON string representation of the object
print(AdvisoryKunbus.to_json())

# convert the object into a dict
advisory_kunbus_dict = advisory_kunbus_instance.to_dict()
# create an instance of AdvisoryKunbus from a dict
advisory_kunbus_from_dict = AdvisoryKunbus.from_dict(advisory_kunbus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


