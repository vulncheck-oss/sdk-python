# AdvisoryShielder


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
from vulncheck_sdk.models.advisory_shielder import AdvisoryShielder

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryShielder from a JSON string
advisory_shielder_instance = AdvisoryShielder.from_json(json)
# print the JSON string representation of the object
print(AdvisoryShielder.to_json())

# convert the object into a dict
advisory_shielder_dict = advisory_shielder_instance.to_dict()
# create an instance of AdvisoryShielder from a dict
advisory_shielder_from_dict = AdvisoryShielder.from_dict(advisory_shielder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


