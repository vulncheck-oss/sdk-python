# AdvisoryNI


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**ovewrview** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ni import AdvisoryNI

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNI from a JSON string
advisory_ni_instance = AdvisoryNI.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNI.to_json())

# convert the object into a dict
advisory_ni_dict = advisory_ni_instance.to_dict()
# create an instance of AdvisoryNI from a dict
advisory_ni_from_dict = AdvisoryNI.from_dict(advisory_ni_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


