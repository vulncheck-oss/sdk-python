# AdvisoryHKCert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**impact** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**related_links** | **List[str]** |  | [optional] 
**risk** | **str** |  | [optional] 
**solutions** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_hk_cert import AdvisoryHKCert

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryHKCert from a JSON string
advisory_hk_cert_instance = AdvisoryHKCert.from_json(json)
# print the JSON string representation of the object
print(AdvisoryHKCert.to_json())

# convert the object into a dict
advisory_hk_cert_dict = advisory_hk_cert_instance.to_dict()
# create an instance of AdvisoryHKCert from a dict
advisory_hk_cert_from_dict = AdvisoryHKCert.from_dict(advisory_hk_cert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


