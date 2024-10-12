# AdvisoryWhatsApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_whats_app import AdvisoryWhatsApp

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryWhatsApp from a JSON string
advisory_whats_app_instance = AdvisoryWhatsApp.from_json(json)
# print the JSON string representation of the object
print(AdvisoryWhatsApp.to_json())

# convert the object into a dict
advisory_whats_app_dict = advisory_whats_app_instance.to_dict()
# create an instance of AdvisoryWhatsApp from a dict
advisory_whats_app_from_dict = AdvisoryWhatsApp.from_dict(advisory_whats_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


