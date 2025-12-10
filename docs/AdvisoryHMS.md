# AdvisoryHMS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_products** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**impact** | **str** |  | [optional] 
**mitigation** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_hms import AdvisoryHMS

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryHMS from a JSON string
advisory_hms_instance = AdvisoryHMS.from_json(json)
# print the JSON string representation of the object
print(AdvisoryHMS.to_json())

# convert the object into a dict
advisory_hms_dict = advisory_hms_instance.to_dict()
# create an instance of AdvisoryHMS from a dict
advisory_hms_from_dict = AdvisoryHMS.from_dict(advisory_hms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


