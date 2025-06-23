# AdvisoryArista


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csaf_url** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_arista import AdvisoryArista

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryArista from a JSON string
advisory_arista_instance = AdvisoryArista.from_json(json)
# print the JSON string representation of the object
print(AdvisoryArista.to_json())

# convert the object into a dict
advisory_arista_dict = advisory_arista_instance.to_dict()
# create an instance of AdvisoryArista from a dict
advisory_arista_from_dict = AdvisoryArista.from_dict(advisory_arista_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


