# ApiEPSSData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **str** |  | [optional] 
**cve** | **str** |  | [optional] 
**epss_percentile** | **float** |  | [optional] 
**epss_score** | **float** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_epss_data import ApiEPSSData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiEPSSData from a JSON string
api_epss_data_instance = ApiEPSSData.from_json(json)
# print the JSON string representation of the object
print(ApiEPSSData.to_json())

# convert the object into a dict
api_epss_data_dict = api_epss_data_instance.to_dict()
# create an instance of ApiEPSSData from a dict
api_epss_data_from_dict = ApiEPSSData.from_dict(api_epss_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


