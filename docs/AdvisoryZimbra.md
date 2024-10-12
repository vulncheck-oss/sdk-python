# AdvisoryZimbra


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bugs** | **List[int]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fix** | **str** |  | [optional] 
**rating** | **str** |  | [optional] 
**reporter** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_zimbra import AdvisoryZimbra

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryZimbra from a JSON string
advisory_zimbra_instance = AdvisoryZimbra.from_json(json)
# print the JSON string representation of the object
print(AdvisoryZimbra.to_json())

# convert the object into a dict
advisory_zimbra_dict = advisory_zimbra_instance.to_dict()
# create an instance of AdvisoryZimbra from a dict
advisory_zimbra_from_dict = AdvisoryZimbra.from_dict(advisory_zimbra_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


