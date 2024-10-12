# AdvisoryQualcomm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chipsets** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**score** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_qualcomm import AdvisoryQualcomm

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryQualcomm from a JSON string
advisory_qualcomm_instance = AdvisoryQualcomm.from_json(json)
# print the JSON string representation of the object
print(AdvisoryQualcomm.to_json())

# convert the object into a dict
advisory_qualcomm_dict = advisory_qualcomm_instance.to_dict()
# create an instance of AdvisoryQualcomm from a dict
advisory_qualcomm_from_dict = AdvisoryQualcomm.from_dict(advisory_qualcomm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


