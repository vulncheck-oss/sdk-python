# AdvisoryVendorNameForThreatActor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threat_actor_name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vendor_name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_vendor_name_for_threat_actor import AdvisoryVendorNameForThreatActor

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryVendorNameForThreatActor from a JSON string
advisory_vendor_name_for_threat_actor_instance = AdvisoryVendorNameForThreatActor.from_json(json)
# print the JSON string representation of the object
print(AdvisoryVendorNameForThreatActor.to_json())

# convert the object into a dict
advisory_vendor_name_for_threat_actor_dict = advisory_vendor_name_for_threat_actor_instance.to_dict()
# create an instance of AdvisoryVendorNameForThreatActor from a dict
advisory_vendor_name_for_threat_actor_from_dict = AdvisoryVendorNameForThreatActor.from_dict(advisory_vendor_name_for_threat_actor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


