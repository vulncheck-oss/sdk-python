# AdvisoryFileCloud


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_file_cloud import AdvisoryFileCloud

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryFileCloud from a JSON string
advisory_file_cloud_instance = AdvisoryFileCloud.from_json(json)
# print the JSON string representation of the object
print(AdvisoryFileCloud.to_json())

# convert the object into a dict
advisory_file_cloud_dict = advisory_file_cloud_instance.to_dict()
# create an instance of AdvisoryFileCloud from a dict
advisory_file_cloud_from_dict = AdvisoryFileCloud.from_dict(advisory_file_cloud_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


