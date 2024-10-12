# AdvisoryApacheSpark


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_apache_spark import AdvisoryApacheSpark

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryApacheSpark from a JSON string
advisory_apache_spark_instance = AdvisoryApacheSpark.from_json(json)
# print the JSON string representation of the object
print(AdvisoryApacheSpark.to_json())

# convert the object into a dict
advisory_apache_spark_dict = advisory_apache_spark_instance.to_dict()
# create an instance of AdvisoryApacheSpark from a dict
advisory_apache_spark_from_dict = AdvisoryApacheSpark.from_dict(advisory_apache_spark_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


