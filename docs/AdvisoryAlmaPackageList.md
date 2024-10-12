# AdvisoryAlmaPackageList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**packages** | [**List[AdvisoryAlmaPackage]**](AdvisoryAlmaPackage.md) |  | [optional] 
**shortname** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_alma_package_list import AdvisoryAlmaPackageList

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAlmaPackageList from a JSON string
advisory_alma_package_list_instance = AdvisoryAlmaPackageList.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAlmaPackageList.to_json())

# convert the object into a dict
advisory_alma_package_list_dict = advisory_alma_package_list_instance.to_dict()
# create an instance of AdvisoryAlmaPackageList from a dict
advisory_alma_package_list_from_dict = AdvisoryAlmaPackageList.from_dict(advisory_alma_package_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


