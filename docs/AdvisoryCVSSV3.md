# AdvisoryCVSSV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attack_complexity** | **str** |  | [optional] 
**attack_vector** | **str** |  | [optional] 
**availability_impact** | **str** |  | [optional] 
**base_score** | **float** |  | [optional] 
**base_severity** | **str** |  | [optional] 
**confidentiality_impact** | **str** |  | [optional] 
**integrity_impact** | **str** |  | [optional] 
**privileges_required** | **str** |  | [optional] 
**scope** | **str** |  | [optional] 
**user_interaction** | **str** |  | [optional] 
**vector_string** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cvssv3 import AdvisoryCVSSV3

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCVSSV3 from a JSON string
advisory_cvssv3_instance = AdvisoryCVSSV3.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCVSSV3.to_json())

# convert the object into a dict
advisory_cvssv3_dict = advisory_cvssv3_instance.to_dict()
# create an instance of AdvisoryCVSSV3 from a dict
advisory_cvssv3_from_dict = AdvisoryCVSSV3.from_dict(advisory_cvssv3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


