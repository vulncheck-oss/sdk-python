# AdvisoryLexmarkAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_products** | [**List[AdvisoryAffectedProduct]**](AdvisoryAffectedProduct.md) |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**details** | **str** |  | [optional] 
**impact** | **str** |  | [optional] 
**last_update** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**public_release_date** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**revision** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**workarounds** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_lexmark_advisory import AdvisoryLexmarkAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryLexmarkAdvisory from a JSON string
advisory_lexmark_advisory_instance = AdvisoryLexmarkAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryLexmarkAdvisory.to_json())

# convert the object into a dict
advisory_lexmark_advisory_dict = advisory_lexmark_advisory_instance.to_dict()
# create an instance of AdvisoryLexmarkAdvisory from a dict
advisory_lexmark_advisory_from_dict = AdvisoryLexmarkAdvisory.from_dict(advisory_lexmark_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


