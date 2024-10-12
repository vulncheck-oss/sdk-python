# AdvisorySyncroSoft


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_syncro_soft import AdvisorySyncroSoft

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySyncroSoft from a JSON string
advisory_syncro_soft_instance = AdvisorySyncroSoft.from_json(json)
# print the JSON string representation of the object
print(AdvisorySyncroSoft.to_json())

# convert the object into a dict
advisory_syncro_soft_dict = advisory_syncro_soft_instance.to_dict()
# create an instance of AdvisorySyncroSoft from a dict
advisory_syncro_soft_from_dict = AdvisorySyncroSoft.from_dict(advisory_syncro_soft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


