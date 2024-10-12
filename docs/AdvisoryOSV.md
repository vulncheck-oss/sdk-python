# AdvisoryOSV


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**date_updated** | **str** |  | [optional] 
**osv** | [**AdvisoryOSVObj**](AdvisoryOSVObj.md) |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_osv import AdvisoryOSV

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOSV from a JSON string
advisory_osv_instance = AdvisoryOSV.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOSV.to_json())

# convert the object into a dict
advisory_osv_dict = advisory_osv_instance.to_dict()
# create an instance of AdvisoryOSV from a dict
advisory_osv_from_dict = AdvisoryOSV.from_dict(advisory_osv_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


