# AdvisoryVulnrichmentContainers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adp** | [**List[AdvisoryADP]**](AdvisoryADP.md) |  | [optional] 
**cna** | [**AdvisoryMCna**](AdvisoryMCna.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_vulnrichment_containers import AdvisoryVulnrichmentContainers

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVulnrichmentContainers from a JSON string
advisory_vulnrichment_containers_instance = AdvisoryVulnrichmentContainers.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVulnrichmentContainers.to_json())

# convert the object into a dict
advisory_vulnrichment_containers_dict = advisory_vulnrichment_containers_instance.to_dict()
# create an instance of AdvisoryVulnrichmentContainers from a dict
advisory_vulnrichment_containers_from_dict = AdvisoryVulnrichmentContainers.from_dict(advisory_vulnrichment_containers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


