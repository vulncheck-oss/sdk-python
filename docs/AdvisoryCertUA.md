# AdvisoryCertUA


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary_ua** | **str** |  | [optional] 
**title_ua** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cert_ua import AdvisoryCertUA

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCertUA from a JSON string
advisory_cert_ua_instance = AdvisoryCertUA.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCertUA.to_json())

# convert the object into a dict
advisory_cert_ua_dict = advisory_cert_ua_instance.to_dict()
# create an instance of AdvisoryCertUA from a dict
advisory_cert_ua_from_dict = AdvisoryCertUA.from_dict(advisory_cert_ua_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


