# AdvisoryAlmaLinuxUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bs_repo_id** | [**AdvisoryAlmaObjectID**](AdvisoryAlmaObjectID.md) |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**fromstr** | **str** |  | [optional] 
**id** | [**AdvisoryAlmaObjectID**](AdvisoryAlmaObjectID.md) |  | [optional] 
**issued_date** | [**AdvisoryAlmaDate**](AdvisoryAlmaDate.md) |  | [optional] 
**pkglist** | [**AdvisoryAlmaPackageList**](AdvisoryAlmaPackageList.md) |  | [optional] 
**pushcount** | **str** |  | [optional] 
**references** | [**List[AdvisoryAlmaReference]**](AdvisoryAlmaReference.md) |  | [optional] 
**release** | **str** |  | [optional] 
**rights** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**solution** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**update_url** | **str** |  | [optional] 
**updated_date** | [**AdvisoryAlmaDate**](AdvisoryAlmaDate.md) |  | [optional] 
**updateinfo_id** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_alma_linux_update import AdvisoryAlmaLinuxUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAlmaLinuxUpdate from a JSON string
advisory_alma_linux_update_instance = AdvisoryAlmaLinuxUpdate.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAlmaLinuxUpdate.to_json())

# convert the object into a dict
advisory_alma_linux_update_dict = advisory_alma_linux_update_instance.to_dict()
# create an instance of AdvisoryAlmaLinuxUpdate from a dict
advisory_alma_linux_update_from_dict = AdvisoryAlmaLinuxUpdate.from_dict(advisory_alma_linux_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


