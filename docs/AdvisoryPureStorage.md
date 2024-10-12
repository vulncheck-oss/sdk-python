# AdvisoryPureStorage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**cvss** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_pure_storage import AdvisoryPureStorage

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPureStorage from a JSON string
advisory_pure_storage_instance = AdvisoryPureStorage.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPureStorage.to_json())

# convert the object into a dict
advisory_pure_storage_dict = advisory_pure_storage_instance.to_dict()
# create an instance of AdvisoryPureStorage from a dict
advisory_pure_storage_from_dict = AdvisoryPureStorage.from_dict(advisory_pure_storage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


