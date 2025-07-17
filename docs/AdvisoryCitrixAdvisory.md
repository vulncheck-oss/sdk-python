# AdvisoryCitrixAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**citrix_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**products** | **List[str]** |  | [optional] 
**severity** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_citrix_advisory import AdvisoryCitrixAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCitrixAdvisory from a JSON string
advisory_citrix_advisory_instance = AdvisoryCitrixAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCitrixAdvisory.to_json())

# convert the object into a dict
advisory_citrix_advisory_dict = advisory_citrix_advisory_instance.to_dict()
# create an instance of AdvisoryCitrixAdvisory from a dict
advisory_citrix_advisory_from_dict = AdvisoryCitrixAdvisory.from_dict(advisory_citrix_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


