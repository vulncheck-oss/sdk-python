# AdvisoryOpenCVDB


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_platforms** | **List[str]** |  | [optional] 
**affected_services** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**disclosed_at** | **str** |  | [optional] 
**known_itw_exploitation** | **bool** |  | [optional] 
**manual_remediation** | **str** |  | [optional] 
**published_at** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_open_cvdb import AdvisoryOpenCVDB

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOpenCVDB from a JSON string
advisory_open_cvdb_instance = AdvisoryOpenCVDB.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOpenCVDB.to_json())

# convert the object into a dict
advisory_open_cvdb_dict = advisory_open_cvdb_instance.to_dict()
# create an instance of AdvisoryOpenCVDB from a dict
advisory_open_cvdb_from_dict = AdvisoryOpenCVDB.from_dict(advisory_open_cvdb_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


