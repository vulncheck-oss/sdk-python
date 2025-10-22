# AdvisoryPKCert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_pk_cert import AdvisoryPKCert

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPKCert from a JSON string
advisory_pk_cert_instance = AdvisoryPKCert.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPKCert.to_json())

# convert the object into a dict
advisory_pk_cert_dict = advisory_pk_cert_instance.to_dict()
# create an instance of AdvisoryPKCert from a dict
advisory_pk_cert_from_dict = AdvisoryPKCert.from_dict(advisory_pk_cert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


