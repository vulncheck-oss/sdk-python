# AdvisoryApacheLoggingServices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_apache_logging_services import AdvisoryApacheLoggingServices

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryApacheLoggingServices from a JSON string
advisory_apache_logging_services_instance = AdvisoryApacheLoggingServices.from_json(json)
# print the JSON string representation of the object
print(AdvisoryApacheLoggingServices.to_json())

# convert the object into a dict
advisory_apache_logging_services_dict = advisory_apache_logging_services_instance.to_dict()
# create an instance of AdvisoryApacheLoggingServices from a dict
advisory_apache_logging_services_from_dict = AdvisoryApacheLoggingServices.from_dict(advisory_apache_logging_services_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


