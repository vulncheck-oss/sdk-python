# AdvisoryGoVulnRanges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[AdvisoryGoEvent]**](AdvisoryGoEvent.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_go_vuln_ranges import AdvisoryGoVulnRanges

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGoVulnRanges from a JSON string
advisory_go_vuln_ranges_instance = AdvisoryGoVulnRanges.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGoVulnRanges.to_json())

# convert the object into a dict
advisory_go_vuln_ranges_dict = advisory_go_vuln_ranges_instance.to_dict()
# create an instance of AdvisoryGoVulnRanges from a dict
advisory_go_vuln_ranges_from_dict = AdvisoryGoVulnRanges.from_dict(advisory_go_vuln_ranges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


