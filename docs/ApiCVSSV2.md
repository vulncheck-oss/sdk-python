# ApiCVSSV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_complexity** | **str** |  | [optional] 
**access_vector** | **str** |  | [optional] 
**authentication** | **str** |  | [optional] 
**availability_impact** | **str** |  | [optional] 
**base_score** | **float** |  | [optional] 
**confidentiality_impact** | **str** |  | [optional] 
**integrity_impact** | **str** |  | [optional] 
**vector_string** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_cvssv2 import ApiCVSSV2

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCVSSV2 from a JSON string
api_cvssv2_instance = ApiCVSSV2.from_json(json)
# print the JSON string representation of the object
print(ApiCVSSV2.to_json())

# convert the object into a dict
api_cvssv2_dict = api_cvssv2_instance.to_dict()
# create an instance of ApiCVSSV2 from a dict
api_cvssv2_from_dict = ApiCVSSV2.from_dict(api_cvssv2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


