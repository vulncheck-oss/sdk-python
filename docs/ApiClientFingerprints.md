# ApiClientFingerprints


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hassh** | **str** |  | [optional] 
**ja3** | **str** |  | [optional] 
**ja4** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_client_fingerprints import ApiClientFingerprints

# TODO update the JSON string below
json = "{}"
# create an instance of ApiClientFingerprints from a JSON string
api_client_fingerprints_instance = ApiClientFingerprints.from_json(json)
# print the JSON string representation of the object
print(ApiClientFingerprints.to_json())

# convert the object into a dict
api_client_fingerprints_dict = api_client_fingerprints_instance.to_dict()
# create an instance of ApiClientFingerprints from a dict
api_client_fingerprints_from_dict = ApiClientFingerprints.from_dict(api_client_fingerprints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


