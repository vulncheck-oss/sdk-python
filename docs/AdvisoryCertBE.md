# AdvisoryCertBE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cert_be import AdvisoryCertBE

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCertBE from a JSON string
advisory_cert_be_instance = AdvisoryCertBE.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCertBE.to_json())

# convert the object into a dict
advisory_cert_be_dict = advisory_cert_be_instance.to_dict()
# create an instance of AdvisoryCertBE from a dict
advisory_cert_be_from_dict = AdvisoryCertBE.from_dict(advisory_cert_be_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


