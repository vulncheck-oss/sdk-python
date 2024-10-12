# AdvisoryCodesysAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codesys_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cwe** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**date_last_revised** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_codesys_advisory import AdvisoryCodesysAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCodesysAdvisory from a JSON string
advisory_codesys_advisory_instance = AdvisoryCodesysAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCodesysAdvisory.to_json())

# convert the object into a dict
advisory_codesys_advisory_dict = advisory_codesys_advisory_instance.to_dict()
# create an instance of AdvisoryCodesysAdvisory from a dict
advisory_codesys_advisory_from_dict = AdvisoryCodesysAdvisory.from_dict(advisory_codesys_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


