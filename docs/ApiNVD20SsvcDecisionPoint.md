# ApiNVD20SsvcDecisionPoint

api.NVD20SsvcDecisionPoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[ApiNVD20SsvcDecisionPointChild]**](ApiNVD20SsvcDecisionPointChild.md) |  | [optional] 
**decision_type** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**options** | [**List[ApiNVD20SsvcDecisionPointOption]**](ApiNVD20SsvcDecisionPointOption.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_ssvc_decision_point import ApiNVD20SsvcDecisionPoint

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20SsvcDecisionPoint from a JSON string
api_nvd20_ssvc_decision_point_instance = ApiNVD20SsvcDecisionPoint.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20SsvcDecisionPoint.to_json())

# convert the object into a dict
api_nvd20_ssvc_decision_point_dict = api_nvd20_ssvc_decision_point_instance.to_dict()
# create an instance of ApiNVD20SsvcDecisionPoint from a dict
api_nvd20_ssvc_decision_point_from_dict = ApiNVD20SsvcDecisionPoint.from_dict(api_nvd20_ssvc_decision_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


