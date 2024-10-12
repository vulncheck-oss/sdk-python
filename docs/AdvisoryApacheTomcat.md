# AdvisoryApacheTomcat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_apache_tomcat import AdvisoryApacheTomcat

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryApacheTomcat from a JSON string
advisory_apache_tomcat_instance = AdvisoryApacheTomcat.from_json(json)
# print the JSON string representation of the object
print(AdvisoryApacheTomcat.to_json())

# convert the object into a dict
advisory_apache_tomcat_dict = advisory_apache_tomcat_instance.to_dict()
# create an instance of AdvisoryApacheTomcat from a dict
advisory_apache_tomcat_from_dict = AdvisoryApacheTomcat.from_dict(advisory_apache_tomcat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


