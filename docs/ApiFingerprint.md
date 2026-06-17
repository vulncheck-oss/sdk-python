# ApiFingerprint

api.Fingerprint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpe** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_fingerprint import ApiFingerprint

# TODO update the JSON string below
json = "{}"
# create an instance of ApiFingerprint from a JSON string
api_fingerprint_instance = ApiFingerprint.from_json(json)
# print the JSON string representation of the object
print(ApiFingerprint.to_json())

# convert the object into a dict
api_fingerprint_dict = api_fingerprint_instance.to_dict()
# create an instance of ApiFingerprint from a dict
api_fingerprint_from_dict = ApiFingerprint.from_dict(api_fingerprint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


