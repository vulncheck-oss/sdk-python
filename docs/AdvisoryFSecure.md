# AdvisoryFSecure


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
from vulncheck_sdk.models.advisory_f_secure import AdvisoryFSecure

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryFSecure from a JSON string
advisory_f_secure_instance = AdvisoryFSecure.from_json(json)
# print the JSON string representation of the object
print(AdvisoryFSecure.to_json())

# convert the object into a dict
advisory_f_secure_dict = advisory_f_secure_instance.to_dict()
# create an instance of AdvisoryFSecure from a dict
advisory_f_secure_from_dict = AdvisoryFSecure.from_dict(advisory_f_secure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


