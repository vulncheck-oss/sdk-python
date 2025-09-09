# AdvisoryCACyberCentreAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control_systems** | **bool** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**html_url** | **str** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ca_cyber_centre_advisory import AdvisoryCACyberCentreAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCACyberCentreAdvisory from a JSON string
advisory_ca_cyber_centre_advisory_instance = AdvisoryCACyberCentreAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCACyberCentreAdvisory.to_json())

# convert the object into a dict
advisory_ca_cyber_centre_advisory_dict = advisory_ca_cyber_centre_advisory_instance.to_dict()
# create an instance of AdvisoryCACyberCentreAdvisory from a dict
advisory_ca_cyber_centre_advisory_from_dict = AdvisoryCACyberCentreAdvisory.from_dict(advisory_ca_cyber_centre_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


