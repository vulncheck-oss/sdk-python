# AdvisoryEOLReleaseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**already_eol** | **bool** |  | [optional] 
**branch** | **str** | Alpine Linux | [optional] 
**branch_url** | **str** | Alpine Linux | [optional] 
**codename** | **str** |  | [optional] 
**cpe** | **str** |  | [optional] 
**eol_date** | **str** |  | [optional] 
**eol_date_extended_support** | **str** | Oracle Linux, Solaris | [optional] 
**eol_date_premier_support** | **str** | Oracle Linux, Solaris | [optional] 
**eol_elts_date** | **str** |  | [optional] 
**eol_lts_date** | **str** |  | [optional] 
**git_branch** | **str** | Alpine Linux | [optional] 
**git_branch_url** | **str** | Alpine Linux | [optional] 
**lts** | **bool** | Ubuntu | [optional] 
**minor_releases** | **List[str]** | Alpine Linux | [optional] 
**product** | **str** |  | [optional] 
**release_date** | **str** |  | [optional] 
**release_name** | **str** |  | [optional] 
**source_url** | **str** |  | [optional] 
**technology_level** | **str** | AIX | [optional] 
**vendor** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**version_api** | **str** | Android | [optional] 
**version_darwin** | **str** | macOS | [optional] 
**version_sunos** | **str** | Solaris | [optional] 
**windows_current_build** | **str** | Microsoft Windows | [optional] 
**windows_display_version** | **str** | Microsoft Windows | [optional] 
**windows_edition_id** | **str** | Microsoft Windows | [optional] 
**windows_insider_preview** | **bool** | Microsoft Windows | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_eol_release_data import AdvisoryEOLReleaseData

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryEOLReleaseData from a JSON string
advisory_eol_release_data_instance = AdvisoryEOLReleaseData.from_json(json)
# print the JSON string representation of the object
print(AdvisoryEOLReleaseData.to_json())

# convert the object into a dict
advisory_eol_release_data_dict = advisory_eol_release_data_instance.to_dict()
# create an instance of AdvisoryEOLReleaseData from a dict
advisory_eol_release_data_from_dict = AdvisoryEOLReleaseData.from_dict(advisory_eol_release_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


