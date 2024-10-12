# AdvisoryCESA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arch** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**issue_date** | **str** |  | [optional] 
**os_release** | **str** |  | [optional] 
**packages** | [**List[AdvisoryCentosPackage]**](AdvisoryCentosPackage.md) |  | [optional] 
**references** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cesa import AdvisoryCESA

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCESA from a JSON string
advisory_cesa_instance = AdvisoryCESA.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCESA.to_json())

# convert the object into a dict
advisory_cesa_dict = advisory_cesa_instance.to_dict()
# create an instance of AdvisoryCESA from a dict
advisory_cesa_from_dict = AdvisoryCESA.from_dict(advisory_cesa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


