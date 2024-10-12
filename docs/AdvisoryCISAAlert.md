# AdvisoryCISAAlert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_products** | **str** |  | [optional] 
**alert_id** | **str** |  | [optional] 
**archived** | **bool** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cveexploited_itw** | **bool** |  | [optional] 
**cvss** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**icsa** | **bool** |  | [optional] 
**icsma** | **bool** |  | [optional] 
**mitigations** | **str** |  | [optional] 
**release_date** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cisa_alert import AdvisoryCISAAlert

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCISAAlert from a JSON string
advisory_cisa_alert_instance = AdvisoryCISAAlert.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCISAAlert.to_json())

# convert the object into a dict
advisory_cisa_alert_dict = advisory_cisa_alert_instance.to_dict()
# create an instance of AdvisoryCISAAlert from a dict
advisory_cisa_alert_from_dict = AdvisoryCISAAlert.from_dict(advisory_cisa_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


