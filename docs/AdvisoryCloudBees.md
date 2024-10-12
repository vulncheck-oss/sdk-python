# AdvisoryCloudBees


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
from vulncheck_sdk.models.advisory_cloud_bees import AdvisoryCloudBees

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCloudBees from a JSON string
advisory_cloud_bees_instance = AdvisoryCloudBees.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCloudBees.to_json())

# convert the object into a dict
advisory_cloud_bees_dict = advisory_cloud_bees_instance.to_dict()
# create an instance of AdvisoryCloudBees from a dict
advisory_cloud_bees_from_dict = AdvisoryCloudBees.from_dict(advisory_cloud_bees_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


