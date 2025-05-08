# AdvisoryHillromAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**cwe** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_hillrom_advisory import AdvisoryHillromAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryHillromAdvisory from a JSON string
advisory_hillrom_advisory_instance = AdvisoryHillromAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryHillromAdvisory.to_json())

# convert the object into a dict
advisory_hillrom_advisory_dict = advisory_hillrom_advisory_instance.to_dict()
# create an instance of AdvisoryHillromAdvisory from a dict
advisory_hillrom_advisory_from_dict = AdvisoryHillromAdvisory.from_dict(advisory_hillrom_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


