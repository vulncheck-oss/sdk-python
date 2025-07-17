# AdvisoryEOLAlibaba


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**eol_date** | **str** |  | [optional] 
**eol_name** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**release_date** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_eol_alibaba import AdvisoryEOLAlibaba

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryEOLAlibaba from a JSON string
advisory_eol_alibaba_instance = AdvisoryEOLAlibaba.from_json(json)
# print the JSON string representation of the object
print(AdvisoryEOLAlibaba.to_json())

# convert the object into a dict
advisory_eol_alibaba_dict = advisory_eol_alibaba_instance.to_dict()
# create an instance of AdvisoryEOLAlibaba from a dict
advisory_eol_alibaba_from_dict = AdvisoryEOLAlibaba.from_dict(advisory_eol_alibaba_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


