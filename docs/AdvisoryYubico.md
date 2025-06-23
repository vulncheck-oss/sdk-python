# AdvisoryYubico


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
from vulncheck_sdk.models.advisory_yubico import AdvisoryYubico

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryYubico from a JSON string
advisory_yubico_instance = AdvisoryYubico.from_json(json)
# print the JSON string representation of the object
print(AdvisoryYubico.to_json())

# convert the object into a dict
advisory_yubico_dict = advisory_yubico_instance.to_dict()
# create an instance of AdvisoryYubico from a dict
advisory_yubico_from_dict = AdvisoryYubico.from_dict(advisory_yubico_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


