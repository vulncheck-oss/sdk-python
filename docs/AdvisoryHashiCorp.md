# AdvisoryHashiCorp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_products** | **str** |  | [optional] 
**background** | **str** |  | [optional] 
**bulletin_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**details** | **str** |  | [optional] 
**remediation** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_hashi_corp import AdvisoryHashiCorp

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryHashiCorp from a JSON string
advisory_hashi_corp_instance = AdvisoryHashiCorp.from_json(json)
# print the JSON string representation of the object
print(AdvisoryHashiCorp.to_json())

# convert the object into a dict
advisory_hashi_corp_dict = advisory_hashi_corp_instance.to_dict()
# create an instance of AdvisoryHashiCorp from a dict
advisory_hashi_corp_from_dict = AdvisoryHashiCorp.from_dict(advisory_hashi_corp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


