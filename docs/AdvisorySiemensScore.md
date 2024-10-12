# AdvisorySiemensScore


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cvss_v3** | [**AdvisorySiemensCVSSV3**](AdvisorySiemensCVSSV3.md) |  | [optional] 
**products** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_siemens_score import AdvisorySiemensScore

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySiemensScore from a JSON string
advisory_siemens_score_instance = AdvisorySiemensScore.from_json(json)
# print the JSON string representation of the object
print(AdvisorySiemensScore.to_json())

# convert the object into a dict
advisory_siemens_score_dict = advisory_siemens_score_instance.to_dict()
# create an instance of AdvisorySiemensScore from a dict
advisory_siemens_score_from_dict = AdvisorySiemensScore.from_dict(advisory_siemens_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


