# AdvisorySierraWireless


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**swid** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_sierra_wireless import AdvisorySierraWireless

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySierraWireless from a JSON string
advisory_sierra_wireless_instance = AdvisorySierraWireless.from_json(json)
# print the JSON string representation of the object
print(AdvisorySierraWireless.to_json())

# convert the object into a dict
advisory_sierra_wireless_dict = advisory_sierra_wireless_instance.to_dict()
# create an instance of AdvisorySierraWireless from a dict
advisory_sierra_wireless_from_dict = AdvisorySierraWireless.from_dict(advisory_sierra_wireless_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


