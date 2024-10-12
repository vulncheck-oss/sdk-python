# AdvisoryOSVObj


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | [**List[AdvisoryAffected]**](AdvisoryAffected.md) | collection based on https://ossf.github.io/osv-schema/ | [optional] 
**aliases** | **List[str]** |  | [optional] 
**details** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**modified** | **str** |  | [optional] 
**published** | **str** |  | [optional] 
**references** | [**List[AdvisoryOSVReference]**](AdvisoryOSVReference.md) |  | [optional] 
**related** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**withdrawn** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_osv_obj import AdvisoryOSVObj

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOSVObj from a JSON string
advisory_osv_obj_instance = AdvisoryOSVObj.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOSVObj.to_json())

# convert the object into a dict
advisory_osv_obj_dict = advisory_osv_obj_instance.to_dict()
# create an instance of AdvisoryOSVObj from a dict
advisory_osv_obj_from_dict = AdvisoryOSVObj.from_dict(advisory_osv_obj_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


