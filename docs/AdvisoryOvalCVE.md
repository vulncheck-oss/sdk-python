# AdvisoryOvalCVE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_oval_cve import AdvisoryOvalCVE

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOvalCVE from a JSON string
advisory_oval_cve_instance = AdvisoryOvalCVE.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOvalCVE.to_json())

# convert the object into a dict
advisory_oval_cve_dict = advisory_oval_cve_instance.to_dict()
# create an instance of AdvisoryOvalCVE from a dict
advisory_oval_cve_from_dict = AdvisoryOvalCVE.from_dict(advisory_oval_cve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


