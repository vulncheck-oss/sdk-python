# AdvisorySingCert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_sing_cert import AdvisorySingCert

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySingCert from a JSON string
advisory_sing_cert_instance = AdvisorySingCert.from_json(json)
# print the JSON string representation of the object
print(AdvisorySingCert.to_json())

# convert the object into a dict
advisory_sing_cert_dict = advisory_sing_cert_instance.to_dict()
# create an instance of AdvisorySingCert from a dict
advisory_sing_cert_from_dict = AdvisorySingCert.from_dict(advisory_sing_cert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


