# AdvisoryOneE


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
from vulncheck_sdk.models.advisory_one_e import AdvisoryOneE

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOneE from a JSON string
advisory_one_e_instance = AdvisoryOneE.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOneE.to_json())

# convert the object into a dict
advisory_one_e_dict = advisory_one_e_instance.to_dict()
# create an instance of AdvisoryOneE from a dict
advisory_one_e_from_dict = AdvisoryOneE.from_dict(advisory_one_e_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


