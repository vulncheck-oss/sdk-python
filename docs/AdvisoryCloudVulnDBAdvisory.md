# AdvisoryCloudVulnDBAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_services** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cloud_vuln_db_advisory import AdvisoryCloudVulnDBAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCloudVulnDBAdvisory from a JSON string
advisory_cloud_vuln_db_advisory_instance = AdvisoryCloudVulnDBAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCloudVulnDBAdvisory.to_json())

# convert the object into a dict
advisory_cloud_vuln_db_advisory_dict = advisory_cloud_vuln_db_advisory_instance.to_dict()
# create an instance of AdvisoryCloudVulnDBAdvisory from a dict
advisory_cloud_vuln_db_advisory_from_dict = AdvisoryCloudVulnDBAdvisory.from_dict(advisory_cloud_vuln_db_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


