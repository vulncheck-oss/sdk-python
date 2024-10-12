# AdvisoryApacheFlink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_apache_flink import AdvisoryApacheFlink

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryApacheFlink from a JSON string
advisory_apache_flink_instance = AdvisoryApacheFlink.from_json(json)
# print the JSON string representation of the object
print(AdvisoryApacheFlink.to_json())

# convert the object into a dict
advisory_apache_flink_dict = advisory_apache_flink_instance.to_dict()
# create an instance of AdvisoryApacheFlink from a dict
advisory_apache_flink_from_dict = AdvisoryApacheFlink.from_dict(advisory_apache_flink_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


