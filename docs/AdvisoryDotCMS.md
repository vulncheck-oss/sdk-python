# AdvisoryDotCMS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**fixed_version** | **str** |  | [optional] 
**issue_id** | **str** |  | [optional] 
**mitigation** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**severity** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_dot_cms import AdvisoryDotCMS

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryDotCMS from a JSON string
advisory_dot_cms_instance = AdvisoryDotCMS.from_json(json)
# print the JSON string representation of the object
print(AdvisoryDotCMS.to_json())

# convert the object into a dict
advisory_dot_cms_dict = advisory_dot_cms_instance.to_dict()
# create an instance of AdvisoryDotCMS from a dict
advisory_dot_cms_from_dict = AdvisoryDotCMS.from_dict(advisory_dot_cms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


