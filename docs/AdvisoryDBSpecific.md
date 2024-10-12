# AdvisoryDBSpecific


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cwe** | [**AdvisoryCurlCWE**](AdvisoryCurlCWE.md) |  | [optional] 
**award** | [**AdvisoryAward**](AdvisoryAward.md) |  | [optional] 
**last_affected** | **str** |  | [optional] 
**package** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**www** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_db_specific import AdvisoryDBSpecific

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryDBSpecific from a JSON string
advisory_db_specific_instance = AdvisoryDBSpecific.from_json(json)
# print the JSON string representation of the object
print(AdvisoryDBSpecific.to_json())

# convert the object into a dict
advisory_db_specific_dict = advisory_db_specific_instance.to_dict()
# create an instance of AdvisoryDBSpecific from a dict
advisory_db_specific_from_dict = AdvisoryDBSpecific.from_dict(advisory_db_specific_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


