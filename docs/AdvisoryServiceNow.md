# AdvisoryServiceNow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_service_now import AdvisoryServiceNow

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryServiceNow from a JSON string
advisory_service_now_instance = AdvisoryServiceNow.from_json(json)
# print the JSON string representation of the object
print(AdvisoryServiceNow.to_json())

# convert the object into a dict
advisory_service_now_dict = advisory_service_now_instance.to_dict()
# create an instance of AdvisoryServiceNow from a dict
advisory_service_now_from_dict = AdvisoryServiceNow.from_dict(advisory_service_now_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


