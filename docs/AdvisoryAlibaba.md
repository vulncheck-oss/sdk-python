# AdvisoryAlibaba


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cnnvd** | **List[str]** |  | [optional] 
**cnvd** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss_score** | **str** |  | [optional] 
**cvss_vector** | **str** |  | [optional] 
**cwe** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**mitigation_cn** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary_cn** | **str** |  | [optional] 
**title_cn** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_alibaba import AdvisoryAlibaba

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAlibaba from a JSON string
advisory_alibaba_instance = AdvisoryAlibaba.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAlibaba.to_json())

# convert the object into a dict
advisory_alibaba_dict = advisory_alibaba_instance.to_dict()
# create an instance of AdvisoryAlibaba from a dict
advisory_alibaba_from_dict = AdvisoryAlibaba.from_dict(advisory_alibaba_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


