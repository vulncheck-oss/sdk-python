# AdvisoryXen


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_xen import AdvisoryXen

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryXen from a JSON string
advisory_xen_instance = AdvisoryXen.from_json(json)
# print the JSON string representation of the object
print(AdvisoryXen.to_json())

# convert the object into a dict
advisory_xen_dict = advisory_xen_instance.to_dict()
# create an instance of AdvisoryXen from a dict
advisory_xen_from_dict = AdvisoryXen.from_dict(advisory_xen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


