# AdvisoryApacheHadoop


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_apache_hadoop import AdvisoryApacheHadoop

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryApacheHadoop from a JSON string
advisory_apache_hadoop_instance = AdvisoryApacheHadoop.from_json(json)
# print the JSON string representation of the object
print(AdvisoryApacheHadoop.to_json())

# convert the object into a dict
advisory_apache_hadoop_dict = advisory_apache_hadoop_instance.to_dict()
# create an instance of AdvisoryApacheHadoop from a dict
advisory_apache_hadoop_from_dict = AdvisoryApacheHadoop.from_dict(advisory_apache_hadoop_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


