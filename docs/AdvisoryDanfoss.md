# AdvisoryDanfoss


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_products** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cve_details** | [**List[AdvisoryDanFossCVEDetails]**](AdvisoryDanFossCVEDetails.md) |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**mitigation** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_danfoss import AdvisoryDanfoss

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryDanfoss from a JSON string
advisory_danfoss_instance = AdvisoryDanfoss.from_json(json)
# print the JSON string representation of the object
print(AdvisoryDanfoss.to_json())

# convert the object into a dict
advisory_danfoss_dict = advisory_danfoss_instance.to_dict()
# create an instance of AdvisoryDanfoss from a dict
advisory_danfoss_from_dict = AdvisoryDanfoss.from_dict(advisory_danfoss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


