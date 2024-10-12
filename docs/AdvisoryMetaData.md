# AdvisoryMetaData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory** | [**AdvisoryAdvisoryDetails**](AdvisoryAdvisoryDetails.md) |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**packages** | [**List[AdvisoryVulnCheckPackage]**](AdvisoryVulnCheckPackage.md) |  | [optional] 
**references** | [**List[AdvisoryOvalReference]**](AdvisoryOvalReference.md) |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_meta_data import AdvisoryMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMetaData from a JSON string
advisory_meta_data_instance = AdvisoryMetaData.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMetaData.to_json())

# convert the object into a dict
advisory_meta_data_dict = advisory_meta_data_instance.to_dict()
# create an instance of AdvisoryMetaData from a dict
advisory_meta_data_from_dict = AdvisoryMetaData.from_dict(advisory_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


