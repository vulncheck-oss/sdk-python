# AdvisoryRockwell


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_products** | [**List[AdvisoryRockwellAffectedProduct]**](AdvisoryRockwellAffectedProduct.md) |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**impact** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_rockwell import AdvisoryRockwell

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRockwell from a JSON string
advisory_rockwell_instance = AdvisoryRockwell.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRockwell.to_json())

# convert the object into a dict
advisory_rockwell_dict = advisory_rockwell_instance.to_dict()
# create an instance of AdvisoryRockwell from a dict
advisory_rockwell_from_dict = AdvisoryRockwell.from_dict(advisory_rockwell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


