# AdvisoryManageEngine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory** | **str** |  | [optional] 
**added_time** | **str** |  | [optional] 
**cve_details_link** | [**AdvisoryCVEDetailsLink**](AdvisoryCVEDetailsLink.md) |  | [optional] 
**cve_id** | **str** |  | [optional] 
**cvss_severity_rating** | **str** |  | [optional] 
**fixed** | **str** |  | [optional] 
**for_product_search** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**product** | [**AdvisoryMEProduct**](AdvisoryMEProduct.md) |  | [optional] 
**product_list** | [**List[AdvisoryMEProduct]**](AdvisoryMEProduct.md) |  | [optional] 
**product_specific_details** | [**List[AdvisoryProductSpecificDetail]**](AdvisoryProductSpecificDetail.md) |  | [optional] 
**summary** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**index_field** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_manage_engine import AdvisoryManageEngine

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryManageEngine from a JSON string
advisory_manage_engine_instance = AdvisoryManageEngine.from_json(json)
# print the JSON string representation of the object
print(AdvisoryManageEngine.to_json())

# convert the object into a dict
advisory_manage_engine_dict = advisory_manage_engine_instance.to_dict()
# create an instance of AdvisoryManageEngine from a dict
advisory_manage_engine_from_dict = AdvisoryManageEngine.from_dict(advisory_manage_engine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


