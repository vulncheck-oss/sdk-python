# AdvisoryVeritas


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulletin_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_veritas import AdvisoryVeritas

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVeritas from a JSON string
advisory_veritas_instance = AdvisoryVeritas.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVeritas.to_json())

# convert the object into a dict
advisory_veritas_dict = advisory_veritas_instance.to_dict()
# create an instance of AdvisoryVeritas from a dict
advisory_veritas_from_dict = AdvisoryVeritas.from_dict(advisory_veritas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


