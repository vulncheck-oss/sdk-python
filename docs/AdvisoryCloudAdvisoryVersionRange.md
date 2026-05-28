# AdvisoryCloudAdvisoryVersionRange

advisory.CloudAdvisoryVersionRange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | **str** |  | [optional] 
**version_end_excluding** | **str** |  | [optional] 
**version_end_including** | **str** |  | [optional] 
**version_start_excluding** | **str** |  | [optional] 
**version_start_including** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cloud_advisory_version_range import AdvisoryCloudAdvisoryVersionRange

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCloudAdvisoryVersionRange from a JSON string
advisory_cloud_advisory_version_range_instance = AdvisoryCloudAdvisoryVersionRange.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCloudAdvisoryVersionRange.to_json())

# convert the object into a dict
advisory_cloud_advisory_version_range_dict = advisory_cloud_advisory_version_range_instance.to_dict()
# create an instance of AdvisoryCloudAdvisoryVersionRange from a dict
advisory_cloud_advisory_version_range_from_dict = AdvisoryCloudAdvisoryVersionRange.from_dict(advisory_cloud_advisory_version_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


