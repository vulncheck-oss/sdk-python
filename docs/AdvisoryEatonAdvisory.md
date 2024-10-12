# AdvisoryEatonAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**cwe** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**eaton_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_eaton_advisory import AdvisoryEatonAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryEatonAdvisory from a JSON string
advisory_eaton_advisory_instance = AdvisoryEatonAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryEatonAdvisory.to_json())

# convert the object into a dict
advisory_eaton_advisory_dict = advisory_eaton_advisory_instance.to_dict()
# create an instance of AdvisoryEatonAdvisory from a dict
advisory_eaton_advisory_from_dict = AdvisoryEatonAdvisory.from_dict(advisory_eaton_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


