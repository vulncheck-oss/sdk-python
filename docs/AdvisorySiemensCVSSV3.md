# AdvisorySiemensCVSSV3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_score** | **float** |  | [optional] 
**base_severity** | **str** |  | [optional] 
**vector_string** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_siemens_cvssv3 import AdvisorySiemensCVSSV3

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySiemensCVSSV3 from a JSON string
advisory_siemens_cvssv3_instance = AdvisorySiemensCVSSV3.from_json(json)
# print the JSON string representation of the object
print(AdvisorySiemensCVSSV3.to_json())

# convert the object into a dict
advisory_siemens_cvssv3_dict = advisory_siemens_cvssv3_instance.to_dict()
# create an instance of AdvisorySiemensCVSSV3 from a dict
advisory_siemens_cvssv3_from_dict = AdvisorySiemensCVSSV3.from_dict(advisory_siemens_cvssv3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


