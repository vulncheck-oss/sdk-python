# AdvisoryApacheNiFi


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_version** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed_versions** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_apache_ni_fi import AdvisoryApacheNiFi

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryApacheNiFi from a JSON string
advisory_apache_ni_fi_instance = AdvisoryApacheNiFi.from_json(json)
# print the JSON string representation of the object
print(AdvisoryApacheNiFi.to_json())

# convert the object into a dict
advisory_apache_ni_fi_dict = advisory_apache_ni_fi_instance.to_dict()
# create an instance of AdvisoryApacheNiFi from a dict
advisory_apache_ni_fi_from_dict = AdvisoryApacheNiFi.from_dict(advisory_apache_ni_fi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


