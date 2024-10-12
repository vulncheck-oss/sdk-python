# AdvisoryAlpineLinuxSecDB


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apkurl** | **str** |  | [optional] 
**archs** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**distroversion** | **str** |  | [optional] 
**packages** | [**List[AdvisoryAlpineLinuxSecDBPackage]**](AdvisoryAlpineLinuxSecDBPackage.md) |  | [optional] 
**reponame** | **str** |  | [optional] 
**urlprefix** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_alpine_linux_sec_db import AdvisoryAlpineLinuxSecDB

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAlpineLinuxSecDB from a JSON string
advisory_alpine_linux_sec_db_instance = AdvisoryAlpineLinuxSecDB.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAlpineLinuxSecDB.to_json())

# convert the object into a dict
advisory_alpine_linux_sec_db_dict = advisory_alpine_linux_sec_db_instance.to_dict()
# create an instance of AdvisoryAlpineLinuxSecDB from a dict
advisory_alpine_linux_sec_db_from_dict = AdvisoryAlpineLinuxSecDB.from_dict(advisory_alpine_linux_sec_db_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


