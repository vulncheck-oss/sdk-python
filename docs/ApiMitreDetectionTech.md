# ApiMitreDetectionTech


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dastacomponent** | **str** |  | [optional] 
**datasource** | **str** |  | [optional] 
**detects** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_mitre_detection_tech import ApiMitreDetectionTech

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMitreDetectionTech from a JSON string
api_mitre_detection_tech_instance = ApiMitreDetectionTech.from_json(json)
# print the JSON string representation of the object
print(ApiMitreDetectionTech.to_json())

# convert the object into a dict
api_mitre_detection_tech_dict = api_mitre_detection_tech_instance.to_dict()
# create an instance of ApiMitreDetectionTech from a dict
api_mitre_detection_tech_from_dict = ApiMitreDetectionTech.from_dict(api_mitre_detection_tech_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


