# AdvisoryGnuTLS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_gnu_tls import AdvisoryGnuTLS

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGnuTLS from a JSON string
advisory_gnu_tls_instance = AdvisoryGnuTLS.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGnuTLS.to_json())

# convert the object into a dict
advisory_gnu_tls_dict = advisory_gnu_tls_instance.to_dict()
# create an instance of AdvisoryGnuTLS from a dict
advisory_gnu_tls_from_dict = AdvisoryGnuTLS.from_dict(advisory_gnu_tls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


