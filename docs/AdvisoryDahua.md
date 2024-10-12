# AdvisoryDahua


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_dahua import AdvisoryDahua

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryDahua from a JSON string
advisory_dahua_instance = AdvisoryDahua.from_json(json)
# print the JSON string representation of the object
print(AdvisoryDahua.to_json())

# convert the object into a dict
advisory_dahua_dict = advisory_dahua_instance.to_dict()
# create an instance of AdvisoryDahua from a dict
advisory_dahua_from_dict = AdvisoryDahua.from_dict(advisory_dahua_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


