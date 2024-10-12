# AdvisoryRenesas


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_renesas import AdvisoryRenesas

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRenesas from a JSON string
advisory_renesas_instance = AdvisoryRenesas.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRenesas.to_json())

# convert the object into a dict
advisory_renesas_dict = advisory_renesas_instance.to_dict()
# create an instance of AdvisoryRenesas from a dict
advisory_renesas_from_dict = AdvisoryRenesas.from_dict(advisory_renesas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


