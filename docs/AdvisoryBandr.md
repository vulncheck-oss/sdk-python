# AdvisoryBandr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**document_id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_bandr import AdvisoryBandr

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBandr from a JSON string
advisory_bandr_instance = AdvisoryBandr.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBandr.to_json())

# convert the object into a dict
advisory_bandr_dict = advisory_bandr_instance.to_dict()
# create an instance of AdvisoryBandr from a dict
advisory_bandr_from_dict = AdvisoryBandr.from_dict(advisory_bandr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


