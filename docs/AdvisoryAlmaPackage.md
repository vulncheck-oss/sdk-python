# AdvisoryAlmaPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arch** | **str** |  | [optional] 
**epoch** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**reboot_suggested** | **int** |  | [optional] 
**release** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**sum** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_alma_package import AdvisoryAlmaPackage

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAlmaPackage from a JSON string
advisory_alma_package_instance = AdvisoryAlmaPackage.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAlmaPackage.to_json())

# convert the object into a dict
advisory_alma_package_dict = advisory_alma_package_instance.to_dict()
# create an instance of AdvisoryAlmaPackage from a dict
advisory_alma_package_from_dict = AdvisoryAlmaPackage.from_dict(advisory_alma_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


