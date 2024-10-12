# AdvisoryNaver


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_naver import AdvisoryNaver

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNaver from a JSON string
advisory_naver_instance = AdvisoryNaver.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNaver.to_json())

# convert the object into a dict
advisory_naver_dict = advisory_naver_instance.to_dict()
# create an instance of AdvisoryNaver from a dict
advisory_naver_from_dict = AdvisoryNaver.from_dict(advisory_naver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


