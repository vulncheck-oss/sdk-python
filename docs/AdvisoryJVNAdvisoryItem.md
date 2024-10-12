# AdvisoryJVNAdvisoryItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpe** | [**List[AdvisoryJVNCPE]**](AdvisoryJVNCPE.md) |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss** | [**List[AdvisoryCVSS]**](AdvisoryCVSS.md) |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**description_en** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 
**issued** | **str** |  | [optional] 
**modified** | **str** |  | [optional] 
**references** | [**List[AdvisoryJVNReference]**](AdvisoryJVNReference.md) |  | [optional] 
**title** | **str** |  | [optional] 
**title_en** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**url_en** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_jvn_advisory_item import AdvisoryJVNAdvisoryItem

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryJVNAdvisoryItem from a JSON string
advisory_jvn_advisory_item_instance = AdvisoryJVNAdvisoryItem.from_json(json)
# print the JSON string representation of the object
print(AdvisoryJVNAdvisoryItem.to_json())

# convert the object into a dict
advisory_jvn_advisory_item_dict = advisory_jvn_advisory_item_instance.to_dict()
# create an instance of AdvisoryJVNAdvisoryItem from a dict
advisory_jvn_advisory_item_from_dict = AdvisoryJVNAdvisoryItem.from_dict(advisory_jvn_advisory_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


