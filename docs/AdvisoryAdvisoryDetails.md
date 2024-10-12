# AdvisoryAdvisoryDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bugzilla** | [**AdvisoryBugzilla**](AdvisoryBugzilla.md) |  | [optional] 
**cve** | [**AdvisoryOvalCVE**](AdvisoryOvalCVE.md) |  | [optional] 
**issued** | [**AdvisoryIssued**](AdvisoryIssued.md) |  | [optional] 
**severity** | **str** |  | [optional] 
**updated** | [**AdvisoryUpdated**](AdvisoryUpdated.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_advisory_details import AdvisoryAdvisoryDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAdvisoryDetails from a JSON string
advisory_advisory_details_instance = AdvisoryAdvisoryDetails.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAdvisoryDetails.to_json())

# convert the object into a dict
advisory_advisory_details_dict = advisory_advisory_details_instance.to_dict()
# create an instance of AdvisoryAdvisoryDetails from a dict
advisory_advisory_details_from_dict = AdvisoryAdvisoryDetails.from_dict(advisory_advisory_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


