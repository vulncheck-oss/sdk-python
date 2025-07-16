# AdvisorySitecore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**refs** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**summary_ja** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**title_ja** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_sitecore import AdvisorySitecore

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySitecore from a JSON string
advisory_sitecore_instance = AdvisorySitecore.from_json(json)
# print the JSON string representation of the object
print(AdvisorySitecore.to_json())

# convert the object into a dict
advisory_sitecore_dict = advisory_sitecore_instance.to_dict()
# create an instance of AdvisorySitecore from a dict
advisory_sitecore_from_dict = AdvisorySitecore.from_dict(advisory_sitecore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


