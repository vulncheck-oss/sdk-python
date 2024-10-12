# AdvisoryK8S


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**issue_id** | **int** |  | [optional] 
**summary** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_k8_s import AdvisoryK8S

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryK8S from a JSON string
advisory_k8_s_instance = AdvisoryK8S.from_json(json)
# print the JSON string representation of the object
print(AdvisoryK8S.to_json())

# convert the object into a dict
advisory_k8_s_dict = advisory_k8_s_instance.to_dict()
# create an instance of AdvisoryK8S from a dict
advisory_k8_s_from_dict = AdvisoryK8S.from_dict(advisory_k8_s_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


