# ApiEPSS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**epss_percentile** | **float** |  | [optional] 
**epss_score** | **float** |  | [optional] 
**last_modified** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_epss import ApiEPSS

# TODO update the JSON string below
json = "{}"
# create an instance of ApiEPSS from a JSON string
api_epss_instance = ApiEPSS.from_json(json)
# print the JSON string representation of the object
print(ApiEPSS.to_json())

# convert the object into a dict
api_epss_dict = api_epss_instance.to_dict()
# create an instance of ApiEPSS from a dict
api_epss_from_dict = ApiEPSS.from_dict(api_epss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


