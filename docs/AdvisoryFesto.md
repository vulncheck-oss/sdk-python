# AdvisoryFesto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csaf_url** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_festo import AdvisoryFesto

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryFesto from a JSON string
advisory_festo_instance = AdvisoryFesto.from_json(json)
# print the JSON string representation of the object
print(AdvisoryFesto.to_json())

# convert the object into a dict
advisory_festo_dict = advisory_festo_instance.to_dict()
# create an instance of AdvisoryFesto from a dict
advisory_festo_from_dict = AdvisoryFesto.from_dict(advisory_festo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


