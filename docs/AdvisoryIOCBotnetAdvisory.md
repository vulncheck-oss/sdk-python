# AdvisoryIOCBotnetAdvisory

advisory.IOCBotnetAdvisory

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**botnet_name** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**malicious_domains** | **List[str]** |  | [optional] 
**malicious_files** | [**List[AdvisoryIOCFile]**](AdvisoryIOCFile.md) |  | [optional] 
**malicious_ip** | **List[str]** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ioc_botnet_advisory import AdvisoryIOCBotnetAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryIOCBotnetAdvisory from a JSON string
advisory_ioc_botnet_advisory_instance = AdvisoryIOCBotnetAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryIOCBotnetAdvisory.to_json())

# convert the object into a dict
advisory_ioc_botnet_advisory_dict = advisory_ioc_botnet_advisory_instance.to_dict()
# create an instance of AdvisoryIOCBotnetAdvisory from a dict
advisory_ioc_botnet_advisory_from_dict = AdvisoryIOCBotnetAdvisory.from_dict(advisory_ioc_botnet_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


