# AdvisorySAP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_sap import AdvisorySAP

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySAP from a JSON string
advisory_sap_instance = AdvisorySAP.from_json(json)
# print the JSON string representation of the object
print(AdvisorySAP.to_json())

# convert the object into a dict
advisory_sap_dict = advisory_sap_instance.to_dict()
# create an instance of AdvisorySAP from a dict
advisory_sap_from_dict = AdvisorySAP.from_dict(advisory_sap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


