# AdvisoryRustsecAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory** | [**AdvisoryRustsecFrontMatterAdvisory**](AdvisoryRustsecFrontMatterAdvisory.md) |  | [optional] 
**affected** | [**AdvisoryRustsecAffected**](AdvisoryRustsecAffected.md) |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**versions** | [**AdvisoryRustsecFrontMatterVersions**](AdvisoryRustsecFrontMatterVersions.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_rustsec_advisory import AdvisoryRustsecAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRustsecAdvisory from a JSON string
advisory_rustsec_advisory_instance = AdvisoryRustsecAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRustsecAdvisory.to_json())

# convert the object into a dict
advisory_rustsec_advisory_dict = advisory_rustsec_advisory_instance.to_dict()
# create an instance of AdvisoryRustsecAdvisory from a dict
advisory_rustsec_advisory_from_dict = AdvisoryRustsecAdvisory.from_dict(advisory_rustsec_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


