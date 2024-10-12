# AdvisoryPhoenixContactAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**cwe** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vde** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_phoenix_contact_advisory import AdvisoryPhoenixContactAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPhoenixContactAdvisory from a JSON string
advisory_phoenix_contact_advisory_instance = AdvisoryPhoenixContactAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPhoenixContactAdvisory.to_json())

# convert the object into a dict
advisory_phoenix_contact_advisory_dict = advisory_phoenix_contact_advisory_instance.to_dict()
# create an instance of AdvisoryPhoenixContactAdvisory from a dict
advisory_phoenix_contact_advisory_from_dict = AdvisoryPhoenixContactAdvisory.from_dict(advisory_phoenix_contact_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


