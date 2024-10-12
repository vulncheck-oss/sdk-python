# AdvisoryOkta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_products** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss** | **str** |  | [optional] 
**cwe** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**resolution** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_okta import AdvisoryOkta

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOkta from a JSON string
advisory_okta_instance = AdvisoryOkta.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOkta.to_json())

# convert the object into a dict
advisory_okta_dict = advisory_okta_instance.to_dict()
# create an instance of AdvisoryOkta from a dict
advisory_okta_from_dict = AdvisoryOkta.from_dict(advisory_okta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


