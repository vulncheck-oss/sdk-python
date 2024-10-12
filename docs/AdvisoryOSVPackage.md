# AdvisoryOSVPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ecosystem** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**purl** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_osv_package import AdvisoryOSVPackage

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOSVPackage from a JSON string
advisory_osv_package_instance = AdvisoryOSVPackage.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOSVPackage.to_json())

# convert the object into a dict
advisory_osv_package_dict = advisory_osv_package_instance.to_dict()
# create an instance of AdvisoryOSVPackage from a dict
advisory_osv_package_from_dict = AdvisoryOSVPackage.from_dict(advisory_osv_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


