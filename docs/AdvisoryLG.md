# AdvisoryLG


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
from vulncheck_sdk.models.advisory_lg import AdvisoryLG

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryLG from a JSON string
advisory_lg_instance = AdvisoryLG.from_json(json)
# print the JSON string representation of the object
print(AdvisoryLG.to_json())

# convert the object into a dict
advisory_lg_dict = advisory_lg_instance.to_dict()
# create an instance of AdvisoryLG from a dict
advisory_lg_from_dict = AdvisoryLG.from_dict(advisory_lg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


