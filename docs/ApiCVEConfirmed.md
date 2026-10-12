# ApiCVEConfirmed

api.CVEConfirmed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confirmed** | **bool** |  | [optional] 
**cve_id** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_cve_confirmed import ApiCVEConfirmed

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCVEConfirmed from a JSON string
api_cve_confirmed_instance = ApiCVEConfirmed.from_json(json)
# print the JSON string representation of the object
print(ApiCVEConfirmed.to_json())

# convert the object into a dict
api_cve_confirmed_dict = api_cve_confirmed_instance.to_dict()
# create an instance of ApiCVEConfirmed from a dict
api_cve_confirmed_from_dict = ApiCVEConfirmed.from_dict(api_cve_confirmed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


