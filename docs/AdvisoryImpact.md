# AdvisoryImpact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capec_id** | **str** |  | [optional] 
**descriptions** | [**List[AdvisoryMDescriptions]**](AdvisoryMDescriptions.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_impact import AdvisoryImpact

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryImpact from a JSON string
advisory_impact_instance = AdvisoryImpact.from_json(json)
# print the JSON string representation of the object
print(AdvisoryImpact.to_json())

# convert the object into a dict
advisory_impact_dict = advisory_impact_instance.to_dict()
# create an instance of AdvisoryImpact from a dict
advisory_impact_from_dict = AdvisoryImpact.from_dict(advisory_impact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


