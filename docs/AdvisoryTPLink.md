# AdvisoryTPLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulletin_id** | **int** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_tp_link import AdvisoryTPLink

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryTPLink from a JSON string
advisory_tp_link_instance = AdvisoryTPLink.from_json(json)
# print the JSON string representation of the object
print(AdvisoryTPLink.to_json())

# convert the object into a dict
advisory_tp_link_dict = advisory_tp_link_instance.to_dict()
# create an instance of AdvisoryTPLink from a dict
advisory_tp_link_from_dict = AdvisoryTPLink.from_dict(advisory_tp_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


