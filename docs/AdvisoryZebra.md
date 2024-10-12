# AdvisoryZebra


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
from vulncheck_sdk.models.advisory_zebra import AdvisoryZebra

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryZebra from a JSON string
advisory_zebra_instance = AdvisoryZebra.from_json(json)
# print the JSON string representation of the object
print(AdvisoryZebra.to_json())

# convert the object into a dict
advisory_zebra_dict = advisory_zebra_instance.to_dict()
# create an instance of AdvisoryZebra from a dict
advisory_zebra_from_dict = AdvisoryZebra.from_dict(advisory_zebra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


