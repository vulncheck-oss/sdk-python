# AdvisoryCiscoKnownGoodValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**biv_category** | **str** |  | [optional] 
**biv_hash** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**dtype** | **str** |  | [optional] 
**filename** | **str** |  | [optional] 
**md5** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**published** | **str** |  | [optional] 
**sha1** | **str** |  | [optional] 
**sha256** | **str** |  | [optional] 
**sha512** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cisco_known_good_value import AdvisoryCiscoKnownGoodValue

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCiscoKnownGoodValue from a JSON string
advisory_cisco_known_good_value_instance = AdvisoryCiscoKnownGoodValue.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCiscoKnownGoodValue.to_json())

# convert the object into a dict
advisory_cisco_known_good_value_dict = advisory_cisco_known_good_value_instance.to_dict()
# create an instance of AdvisoryCiscoKnownGoodValue from a dict
advisory_cisco_known_good_value_from_dict = AdvisoryCiscoKnownGoodValue.from_dict(advisory_cisco_known_good_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


