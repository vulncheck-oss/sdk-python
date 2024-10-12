# AdvisoryDNN


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
from vulncheck_sdk.models.advisory_dnn import AdvisoryDNN

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryDNN from a JSON string
advisory_dnn_instance = AdvisoryDNN.from_json(json)
# print the JSON string representation of the object
print(AdvisoryDNN.to_json())

# convert the object into a dict
advisory_dnn_dict = advisory_dnn_instance.to_dict()
# create an instance of AdvisoryDNN from a dict
advisory_dnn_from_dict = AdvisoryDNN.from_dict(advisory_dnn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


