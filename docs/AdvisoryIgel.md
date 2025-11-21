# AdvisoryIgel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**cvss_score** | **str** |  | [optional] 
**cvss_vector** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_igel import AdvisoryIgel

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryIgel from a JSON string
advisory_igel_instance = AdvisoryIgel.from_json(json)
# print the JSON string representation of the object
print(AdvisoryIgel.to_json())

# convert the object into a dict
advisory_igel_dict = advisory_igel_instance.to_dict()
# create an instance of AdvisoryIgel from a dict
advisory_igel_from_dict = AdvisoryIgel.from_dict(advisory_igel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


