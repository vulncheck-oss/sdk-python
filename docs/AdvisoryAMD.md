# AdvisoryAMD


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulletin_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**date_updated** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_amd import AdvisoryAMD

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAMD from a JSON string
advisory_amd_instance = AdvisoryAMD.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAMD.to_json())

# convert the object into a dict
advisory_amd_dict = advisory_amd_instance.to_dict()
# create an instance of AdvisoryAMD from a dict
advisory_amd_from_dict = AdvisoryAMD.from_dict(advisory_amd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


