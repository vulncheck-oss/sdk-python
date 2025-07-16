# AdvisoryNessus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpe** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**exploitability_ease** | **str** | seems like only 3 vals for this | [optional] 
**filename** | **str** |  | [optional] 
**iava** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**script_id** | **int** |  | [optional] 
**updated** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_nessus import AdvisoryNessus

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNessus from a JSON string
advisory_nessus_instance = AdvisoryNessus.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNessus.to_json())

# convert the object into a dict
advisory_nessus_dict = advisory_nessus_instance.to_dict()
# create an instance of AdvisoryNessus from a dict
advisory_nessus_from_dict = AdvisoryNessus.from_dict(advisory_nessus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


