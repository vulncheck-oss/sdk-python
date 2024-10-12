# AdvisoryHoneywell


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
from vulncheck_sdk.models.advisory_honeywell import AdvisoryHoneywell

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryHoneywell from a JSON string
advisory_honeywell_instance = AdvisoryHoneywell.from_json(json)
# print the JSON string representation of the object
print(AdvisoryHoneywell.to_json())

# convert the object into a dict
advisory_honeywell_dict = advisory_honeywell_instance.to_dict()
# create an instance of AdvisoryHoneywell from a dict
advisory_honeywell_from_dict = AdvisoryHoneywell.from_dict(advisory_honeywell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


