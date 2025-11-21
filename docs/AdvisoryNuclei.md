# AdvisoryNuclei


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**template** | **object** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_nuclei import AdvisoryNuclei

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNuclei from a JSON string
advisory_nuclei_instance = AdvisoryNuclei.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNuclei.to_json())

# convert the object into a dict
advisory_nuclei_dict = advisory_nuclei_instance.to_dict()
# create an instance of AdvisoryNuclei from a dict
advisory_nuclei_from_dict = AdvisoryNuclei.from_dict(advisory_nuclei_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


