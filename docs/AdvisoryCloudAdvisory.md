# AdvisoryCloudAdvisory

advisory.CloudAdvisory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_versions** | [**List[AdvisoryCloudAdvisoryVersionRange]**](AdvisoryCloudAdvisoryVersionRange.md) |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**service** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cloud_advisory import AdvisoryCloudAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCloudAdvisory from a JSON string
advisory_cloud_advisory_instance = AdvisoryCloudAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCloudAdvisory.to_json())

# convert the object into a dict
advisory_cloud_advisory_dict = advisory_cloud_advisory_instance.to_dict()
# create an instance of AdvisoryCloudAdvisory from a dict
advisory_cloud_advisory_from_dict = AdvisoryCloudAdvisory.from_dict(advisory_cloud_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


