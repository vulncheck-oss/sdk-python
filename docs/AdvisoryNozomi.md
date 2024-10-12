# AdvisoryNozomi


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_nozomi import AdvisoryNozomi

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNozomi from a JSON string
advisory_nozomi_instance = AdvisoryNozomi.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNozomi.to_json())

# convert the object into a dict
advisory_nozomi_dict = advisory_nozomi_instance.to_dict()
# create an instance of AdvisoryNozomi from a dict
advisory_nozomi_from_dict = AdvisoryNozomi.from_dict(advisory_nozomi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


