# AdvisoryIsraeliAlert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**details_he** | **str** |  | [optional] 
**handling_he** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary_he** | **str** |  | [optional] 
**title_he** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_israeli_alert import AdvisoryIsraeliAlert

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryIsraeliAlert from a JSON string
advisory_israeli_alert_instance = AdvisoryIsraeliAlert.from_json(json)
# print the JSON string representation of the object
print(AdvisoryIsraeliAlert.to_json())

# convert the object into a dict
advisory_israeli_alert_dict = advisory_israeli_alert_instance.to_dict()
# create an instance of AdvisoryIsraeliAlert from a dict
advisory_israeli_alert_from_dict = AdvisoryIsraeliAlert.from_dict(advisory_israeli_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


