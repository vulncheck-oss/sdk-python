# AdvisoryMACert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_systems_fr** | **str** |  | [optional] 
**assessment_fr** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**impact_fr** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**risk_fr** | **str** |  | [optional] 
**risks_fr** | **str** |  | [optional] 
**solution_fr** | **str** |  | [optional] 
**title_fr** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ma_cert import AdvisoryMACert

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMACert from a JSON string
advisory_ma_cert_instance = AdvisoryMACert.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMACert.to_json())

# convert the object into a dict
advisory_ma_cert_dict = advisory_ma_cert_instance.to_dict()
# create an instance of AdvisoryMACert from a dict
advisory_ma_cert_from_dict = AdvisoryMACert.from_dict(advisory_ma_cert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


