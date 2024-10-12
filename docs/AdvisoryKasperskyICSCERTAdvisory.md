# AdvisoryKasperskyICSCERTAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**cwe** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**klcert_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_kaspersky_icscert_advisory import AdvisoryKasperskyICSCERTAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryKasperskyICSCERTAdvisory from a JSON string
advisory_kaspersky_icscert_advisory_instance = AdvisoryKasperskyICSCERTAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryKasperskyICSCERTAdvisory.to_json())

# convert the object into a dict
advisory_kaspersky_icscert_advisory_dict = advisory_kaspersky_icscert_advisory_instance.to_dict()
# create an instance of AdvisoryKasperskyICSCERTAdvisory from a dict
advisory_kaspersky_icscert_advisory_from_dict = AdvisoryKasperskyICSCERTAdvisory.from_dict(advisory_kaspersky_icscert_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


