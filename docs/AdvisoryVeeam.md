# AdvisoryVeeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**details** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**solution** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_veeam import AdvisoryVeeam

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVeeam from a JSON string
advisory_veeam_instance = AdvisoryVeeam.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVeeam.to_json())

# convert the object into a dict
advisory_veeam_dict = advisory_veeam_instance.to_dict()
# create an instance of AdvisoryVeeam from a dict
advisory_veeam_from_dict = AdvisoryVeeam.from_dict(advisory_veeam_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


