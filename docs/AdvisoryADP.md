# AdvisoryADP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | [**List[AdvisoryMAffected]**](AdvisoryMAffected.md) |  | [optional] 
**metrics** | [**List[AdvisoryVulnrichmentMetric]**](AdvisoryVulnrichmentMetric.md) |  | [optional] 
**provider_metadata** | [**AdvisoryMProviderMetadata**](AdvisoryMProviderMetadata.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_adp import AdvisoryADP

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryADP from a JSON string
advisory_adp_instance = AdvisoryADP.from_json(json)
# print the JSON string representation of the object
print(AdvisoryADP.to_json())

# convert the object into a dict
advisory_adp_dict = advisory_adp_instance.to_dict()
# create an instance of AdvisoryADP from a dict
advisory_adp_from_dict = AdvisoryADP.from_dict(advisory_adp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


