# AdvisoryApacheCamel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_apache_camel import AdvisoryApacheCamel

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryApacheCamel from a JSON string
advisory_apache_camel_instance = AdvisoryApacheCamel.from_json(json)
# print the JSON string representation of the object
print(AdvisoryApacheCamel.to_json())

# convert the object into a dict
advisory_apache_camel_dict = advisory_apache_camel_instance.to_dict()
# create an instance of AdvisoryApacheCamel from a dict
advisory_apache_camel_from_dict = AdvisoryApacheCamel.from_dict(advisory_apache_camel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


