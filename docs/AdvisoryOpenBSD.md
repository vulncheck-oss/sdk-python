# AdvisoryOpenBSD


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**patch** | **str** |  | [optional] 
**release** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_open_bsd import AdvisoryOpenBSD

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOpenBSD from a JSON string
advisory_open_bsd_instance = AdvisoryOpenBSD.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOpenBSD.to_json())

# convert the object into a dict
advisory_open_bsd_dict = advisory_open_bsd_instance.to_dict()
# create an instance of AdvisoryOpenBSD from a dict
advisory_open_bsd_from_dict = AdvisoryOpenBSD.from_dict(advisory_open_bsd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


