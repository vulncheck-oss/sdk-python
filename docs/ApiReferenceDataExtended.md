# ApiReferenceDataExtended


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_added** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**lang** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**previous_url** | **str** |  | [optional] 
**refsource** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_reference_data_extended import ApiReferenceDataExtended

# TODO update the JSON string below
json = "{}"
# create an instance of ApiReferenceDataExtended from a JSON string
api_reference_data_extended_instance = ApiReferenceDataExtended.from_json(json)
# print the JSON string representation of the object
print(ApiReferenceDataExtended.to_json())

# convert the object into a dict
api_reference_data_extended_dict = api_reference_data_extended_instance.to_dict()
# create an instance of ApiReferenceDataExtended from a dict
api_reference_data_extended_from_dict = ApiReferenceDataExtended.from_dict(api_reference_data_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


