# AdvisoryGHSA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**ghsa** | [**AdvisoryOriginalGHSA**](AdvisoryOriginalGHSA.md) |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ghsa import AdvisoryGHSA

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGHSA from a JSON string
advisory_ghsa_instance = AdvisoryGHSA.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGHSA.to_json())

# convert the object into a dict
advisory_ghsa_dict = advisory_ghsa_instance.to_dict()
# create an instance of AdvisoryGHSA from a dict
advisory_ghsa_from_dict = AdvisoryGHSA.from_dict(advisory_ghsa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


