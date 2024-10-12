# AdvisoryRustsecAffected


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arch** | **List[str]** |  | [optional] 
**functions** | **str** |  | [optional] 
**os** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_rustsec_affected import AdvisoryRustsecAffected

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRustsecAffected from a JSON string
advisory_rustsec_affected_instance = AdvisoryRustsecAffected.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRustsecAffected.to_json())

# convert the object into a dict
advisory_rustsec_affected_dict = advisory_rustsec_affected_instance.to_dict()
# create an instance of AdvisoryRustsecAffected from a dict
advisory_rustsec_affected_from_dict = AdvisoryRustsecAffected.from_dict(advisory_rustsec_affected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


