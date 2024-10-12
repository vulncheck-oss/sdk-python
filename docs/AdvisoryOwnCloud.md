# AdvisoryOwnCloud


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
from vulncheck_sdk.models.advisory_own_cloud import AdvisoryOwnCloud

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOwnCloud from a JSON string
advisory_own_cloud_instance = AdvisoryOwnCloud.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOwnCloud.to_json())

# convert the object into a dict
advisory_own_cloud_dict = advisory_own_cloud_instance.to_dict()
# create an instance of AdvisoryOwnCloud from a dict
advisory_own_cloud_from_dict = AdvisoryOwnCloud.from_dict(advisory_own_cloud_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


