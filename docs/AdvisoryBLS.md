# AdvisoryBLS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**cvss** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**prodcut** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_bls import AdvisoryBLS

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBLS from a JSON string
advisory_bls_instance = AdvisoryBLS.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBLS.to_json())

# convert the object into a dict
advisory_bls_dict = advisory_bls_instance.to_dict()
# create an instance of AdvisoryBLS from a dict
advisory_bls_from_dict = AdvisoryBLS.from_dict(advisory_bls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


