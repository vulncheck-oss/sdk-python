# AdvisoryApacheKafka


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_apache_kafka import AdvisoryApacheKafka

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryApacheKafka from a JSON string
advisory_apache_kafka_instance = AdvisoryApacheKafka.from_json(json)
# print the JSON string representation of the object
print(AdvisoryApacheKafka.to_json())

# convert the object into a dict
advisory_apache_kafka_dict = advisory_apache_kafka_instance.to_dict()
# create an instance of AdvisoryApacheKafka from a dict
advisory_apache_kafka_from_dict = AdvisoryApacheKafka.from_dict(advisory_apache_kafka_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


