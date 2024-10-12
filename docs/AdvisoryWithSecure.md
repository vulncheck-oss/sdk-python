# AdvisoryWithSecure


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
from vulncheck_sdk.models.advisory_with_secure import AdvisoryWithSecure

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryWithSecure from a JSON string
advisory_with_secure_instance = AdvisoryWithSecure.from_json(json)
# print the JSON string representation of the object
print(AdvisoryWithSecure.to_json())

# convert the object into a dict
advisory_with_secure_dict = advisory_with_secure_instance.to_dict()
# create an instance of AdvisoryWithSecure from a dict
advisory_with_secure_from_dict = AdvisoryWithSecure.from_dict(advisory_with_secure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


