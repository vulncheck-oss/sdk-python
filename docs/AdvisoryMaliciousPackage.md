# AdvisoryMaliciousPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**malware** | [**AdvisoryOSVObj**](AdvisoryOSVObj.md) |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_malicious_package import AdvisoryMaliciousPackage

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMaliciousPackage from a JSON string
advisory_malicious_package_instance = AdvisoryMaliciousPackage.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMaliciousPackage.to_json())

# convert the object into a dict
advisory_malicious_package_dict = advisory_malicious_package_instance.to_dict()
# create an instance of AdvisoryMaliciousPackage from a dict
advisory_malicious_package_from_dict = AdvisoryMaliciousPackage.from_dict(advisory_malicious_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


