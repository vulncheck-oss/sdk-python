# AdvisoryAruba


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csaf** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_aruba import AdvisoryAruba

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAruba from a JSON string
advisory_aruba_instance = AdvisoryAruba.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAruba.to_json())

# convert the object into a dict
advisory_aruba_dict = advisory_aruba_instance.to_dict()
# create an instance of AdvisoryAruba from a dict
advisory_aruba_from_dict = AdvisoryAruba.from_dict(advisory_aruba_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


