# AdvisoryMbedTLS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affects** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_mbed_tls import AdvisoryMbedTLS

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMbedTLS from a JSON string
advisory_mbed_tls_instance = AdvisoryMbedTLS.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMbedTLS.to_json())

# convert the object into a dict
advisory_mbed_tls_dict = advisory_mbed_tls_instance.to_dict()
# create an instance of AdvisoryMbedTLS from a dict
advisory_mbed_tls_from_dict = AdvisoryMbedTLS.from_dict(advisory_mbed_tls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


