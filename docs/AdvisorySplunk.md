# AdvisorySplunk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory_id** | **str** |  | [optional] 
**affected_products** | [**List[AdvisorySplunkProduct]**](AdvisorySplunkProduct.md) |  | [optional] 
**bug_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_splunk import AdvisorySplunk

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySplunk from a JSON string
advisory_splunk_instance = AdvisorySplunk.from_json(json)
# print the JSON string representation of the object
print(AdvisorySplunk.to_json())

# convert the object into a dict
advisory_splunk_dict = advisory_splunk_instance.to_dict()
# create an instance of AdvisorySplunk from a dict
advisory_splunk_from_dict = AdvisorySplunk.from_dict(advisory_splunk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


