# AdvisoryTailscale


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_tailscale import AdvisoryTailscale

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryTailscale from a JSON string
advisory_tailscale_instance = AdvisoryTailscale.from_json(json)
# print the JSON string representation of the object
print(AdvisoryTailscale.to_json())

# convert the object into a dict
advisory_tailscale_dict = advisory_tailscale_instance.to_dict()
# create an instance of AdvisoryTailscale from a dict
advisory_tailscale_from_dict = AdvisoryTailscale.from_dict(advisory_tailscale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


