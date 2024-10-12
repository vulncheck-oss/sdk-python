# AdvisoryAbbott


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_abbott import AdvisoryAbbott

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAbbott from a JSON string
advisory_abbott_instance = AdvisoryAbbott.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAbbott.to_json())

# convert the object into a dict
advisory_abbott_dict = advisory_abbott_instance.to_dict()
# create an instance of AdvisoryAbbott from a dict
advisory_abbott_from_dict = AdvisoryAbbott.from_dict(advisory_abbott_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


