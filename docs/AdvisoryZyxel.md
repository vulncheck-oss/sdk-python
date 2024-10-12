# AdvisoryZyxel


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
from vulncheck_sdk.models.advisory_zyxel import AdvisoryZyxel

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryZyxel from a JSON string
advisory_zyxel_instance = AdvisoryZyxel.from_json(json)
# print the JSON string representation of the object
print(AdvisoryZyxel.to_json())

# convert the object into a dict
advisory_zyxel_dict = advisory_zyxel_instance.to_dict()
# create an instance of AdvisoryZyxel from a dict
advisory_zyxel_from_dict = AdvisoryZyxel.from_dict(advisory_zyxel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


