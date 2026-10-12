# ApiNVD20SsvcDataV203

api.NVD20SsvcDataV203

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** |  | [optional] 
**computed** | **str** |  | [optional] 
**decision_tree** | [**ApiNVD20SsvcDecisionTree**](ApiNVD20SsvcDecisionTree.md) |  | [optional] 
**decision_tree_url** | **str** |  | [optional] 
**generator** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**options** | [**List[ApiNVD20SsvcOption]**](ApiNVD20SsvcOption.md) |  | [optional] 
**role** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_ssvc_data_v203 import ApiNVD20SsvcDataV203

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20SsvcDataV203 from a JSON string
api_nvd20_ssvc_data_v203_instance = ApiNVD20SsvcDataV203.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20SsvcDataV203.to_json())

# convert the object into a dict
api_nvd20_ssvc_data_v203_dict = api_nvd20_ssvc_data_v203_instance.to_dict()
# create an instance of ApiNVD20SsvcDataV203 from a dict
api_nvd20_ssvc_data_v203_from_dict = ApiNVD20SsvcDataV203.from_dict(api_nvd20_ssvc_data_v203_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


