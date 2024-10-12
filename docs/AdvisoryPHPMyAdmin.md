# AdvisoryPHPMyAdmin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_phpmy_admin import AdvisoryPHPMyAdmin

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPHPMyAdmin from a JSON string
advisory_phpmy_admin_instance = AdvisoryPHPMyAdmin.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPHPMyAdmin.to_json())

# convert the object into a dict
advisory_phpmy_admin_dict = advisory_phpmy_admin_instance.to_dict()
# create an instance of AdvisoryPHPMyAdmin from a dict
advisory_phpmy_admin_from_dict = AdvisoryPHPMyAdmin.from_dict(advisory_phpmy_admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


