# AdvisoryCertSE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary_sv** | **str** |  | [optional] 
**title_sv** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cert_se import AdvisoryCertSE

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCertSE from a JSON string
advisory_cert_se_instance = AdvisoryCertSE.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCertSE.to_json())

# convert the object into a dict
advisory_cert_se_dict = advisory_cert_se_instance.to_dict()
# create an instance of AdvisoryCertSE from a dict
advisory_cert_se_from_dict = AdvisoryCertSE.from_dict(advisory_cert_se_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


