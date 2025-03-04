# AdvisoryDell


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**article_number** | **str** |  | [optional] 
**combined_product_list** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**dell_cves** | [**List[AdvisoryDellCVE]**](AdvisoryDellCVE.md) |  | [optional] 
**severity** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_dell import AdvisoryDell

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryDell from a JSON string
advisory_dell_instance = AdvisoryDell.from_json(json)
# print the JSON string representation of the object
print(AdvisoryDell.to_json())

# convert the object into a dict
advisory_dell_dict = advisory_dell_instance.to_dict()
# create an instance of AdvisoryDell from a dict
advisory_dell_from_dict = AdvisoryDell.from_dict(advisory_dell_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


