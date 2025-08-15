# AdvisoryDLink


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
from vulncheck_sdk.models.advisory_d_link import AdvisoryDLink

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryDLink from a JSON string
advisory_d_link_instance = AdvisoryDLink.from_json(json)
# print the JSON string representation of the object
print(AdvisoryDLink.to_json())

# convert the object into a dict
advisory_d_link_dict = advisory_d_link_instance.to_dict()
# create an instance of AdvisoryDLink from a dict
advisory_d_link_from_dict = AdvisoryDLink.from_dict(advisory_d_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


