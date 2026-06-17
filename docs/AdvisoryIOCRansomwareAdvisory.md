# AdvisoryIOCRansomwareAdvisory

advisory.IOCRansomwareAdvisory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**malicious_domains** | **List[str]** |  | [optional] 
**malicious_files** | [**List[AdvisoryIOCFile]**](AdvisoryIOCFile.md) |  | [optional] 
**malicious_ip** | **List[str]** |  | [optional] 
**ransomware_name** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ioc_ransomware_advisory import AdvisoryIOCRansomwareAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryIOCRansomwareAdvisory from a JSON string
advisory_ioc_ransomware_advisory_instance = AdvisoryIOCRansomwareAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryIOCRansomwareAdvisory.to_json())

# convert the object into a dict
advisory_ioc_ransomware_advisory_dict = advisory_ioc_ransomware_advisory_instance.to_dict()
# create an instance of AdvisoryIOCRansomwareAdvisory from a dict
advisory_ioc_ransomware_advisory_from_dict = AdvisoryIOCRansomwareAdvisory.from_dict(advisory_ioc_ransomware_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


