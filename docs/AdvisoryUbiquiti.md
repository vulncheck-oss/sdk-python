# AdvisoryUbiquiti


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**links** | **List[str]** |  | [optional] 
**products** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ubiquiti import AdvisoryUbiquiti

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryUbiquiti from a JSON string
advisory_ubiquiti_instance = AdvisoryUbiquiti.from_json(json)
# print the JSON string representation of the object
print(AdvisoryUbiquiti.to_json())

# convert the object into a dict
advisory_ubiquiti_dict = advisory_ubiquiti_instance.to_dict()
# create an instance of AdvisoryUbiquiti from a dict
advisory_ubiquiti_from_dict = AdvisoryUbiquiti.from_dict(advisory_ubiquiti_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


