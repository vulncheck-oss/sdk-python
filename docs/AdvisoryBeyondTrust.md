# AdvisoryBeyondTrust


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_beyond_trust import AdvisoryBeyondTrust

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBeyondTrust from a JSON string
advisory_beyond_trust_instance = AdvisoryBeyondTrust.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBeyondTrust.to_json())

# convert the object into a dict
advisory_beyond_trust_dict = advisory_beyond_trust_instance.to_dict()
# create an instance of AdvisoryBeyondTrust from a dict
advisory_beyond_trust_from_dict = AdvisoryBeyondTrust.from_dict(advisory_beyond_trust_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


