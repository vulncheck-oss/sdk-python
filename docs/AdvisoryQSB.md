# AdvisoryQSB


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_qsb import AdvisoryQSB

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryQSB from a JSON string
advisory_qsb_instance = AdvisoryQSB.from_json(json)
# print the JSON string representation of the object
print(AdvisoryQSB.to_json())

# convert the object into a dict
advisory_qsb_dict = advisory_qsb_instance.to_dict()
# create an instance of AdvisoryQSB from a dict
advisory_qsb_from_dict = AdvisoryQSB.from_dict(advisory_qsb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


