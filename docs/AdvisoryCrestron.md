# AdvisoryCrestron


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**threat** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_crestron import AdvisoryCrestron

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCrestron from a JSON string
advisory_crestron_instance = AdvisoryCrestron.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCrestron.to_json())

# convert the object into a dict
advisory_crestron_dict = advisory_crestron_instance.to_dict()
# create an instance of AdvisoryCrestron from a dict
advisory_crestron_from_dict = AdvisoryCrestron.from_dict(advisory_crestron_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


