# AdvisoryMAffected


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_url** | **str** |  | [optional] 
**cpes** | **List[str]** |  | [optional] 
**default_status** | **str** |  | [optional] 
**package_name** | **str** |  | [optional] 
**platforms** | **List[str]** |  | [optional] 
**product** | **str** |  | [optional] 
**repos** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 
**versions** | [**List[AdvisoryMVersion]**](AdvisoryMVersion.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_m_affected import AdvisoryMAffected

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMAffected from a JSON string
advisory_m_affected_instance = AdvisoryMAffected.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMAffected.to_json())

# convert the object into a dict
advisory_m_affected_dict = advisory_m_affected_instance.to_dict()
# create an instance of AdvisoryMAffected from a dict
advisory_m_affected_from_dict = AdvisoryMAffected.from_dict(advisory_m_affected_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


