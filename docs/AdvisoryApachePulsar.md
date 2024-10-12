# AdvisoryApachePulsar


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_apache_pulsar import AdvisoryApachePulsar

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryApachePulsar from a JSON string
advisory_apache_pulsar_instance = AdvisoryApachePulsar.from_json(json)
# print the JSON string representation of the object
print(AdvisoryApachePulsar.to_json())

# convert the object into a dict
advisory_apache_pulsar_dict = advisory_apache_pulsar_instance.to_dict()
# create an instance of AdvisoryApachePulsar from a dict
advisory_apache_pulsar_from_dict = AdvisoryApachePulsar.from_dict(advisory_apache_pulsar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


