# AdvisoryPowerDNS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_power_dns import AdvisoryPowerDNS

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPowerDNS from a JSON string
advisory_power_dns_instance = AdvisoryPowerDNS.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPowerDNS.to_json())

# convert the object into a dict
advisory_power_dns_dict = advisory_power_dns_instance.to_dict()
# create an instance of AdvisoryPowerDNS from a dict
advisory_power_dns_from_dict = AdvisoryPowerDNS.from_dict(advisory_power_dns_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


