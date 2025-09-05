# ApiMitreMitigationTech


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**mitigation_url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_mitre_mitigation_tech import ApiMitreMitigationTech

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMitreMitigationTech from a JSON string
api_mitre_mitigation_tech_instance = ApiMitreMitigationTech.from_json(json)
# print the JSON string representation of the object
print(ApiMitreMitigationTech.to_json())

# convert the object into a dict
api_mitre_mitigation_tech_dict = api_mitre_mitigation_tech_instance.to_dict()
# create an instance of ApiMitreMitigationTech from a dict
api_mitre_mitigation_tech_from_dict = ApiMitreMitigationTech.from_dict(api_mitre_mitigation_tech_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


