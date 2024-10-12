# ApiReferenceData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**refsource** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_reference_data import ApiReferenceData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiReferenceData from a JSON string
api_reference_data_instance = ApiReferenceData.from_json(json)
# print the JSON string representation of the object
print(ApiReferenceData.to_json())

# convert the object into a dict
api_reference_data_dict = api_reference_data_instance.to_dict()
# create an instance of ApiReferenceData from a dict
api_reference_data_from_dict = ApiReferenceData.from_dict(api_reference_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


