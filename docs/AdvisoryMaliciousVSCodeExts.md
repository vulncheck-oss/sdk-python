# AdvisoryMaliciousVSCodeExts

advisory.MaliciousVSCodeExts

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_added** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**publisher** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **str** | the data in this feed comes from manual curation. so this will likely be omitted. | [optional] 
**url** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_malicious_vs_code_exts import AdvisoryMaliciousVSCodeExts

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMaliciousVSCodeExts from a JSON string
advisory_malicious_vs_code_exts_instance = AdvisoryMaliciousVSCodeExts.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMaliciousVSCodeExts.to_json())

# convert the object into a dict
advisory_malicious_vs_code_exts_dict = advisory_malicious_vs_code_exts_instance.to_dict()
# create an instance of AdvisoryMaliciousVSCodeExts from a dict
advisory_malicious_vs_code_exts_from_dict = AdvisoryMaliciousVSCodeExts.from_dict(advisory_malicious_vs_code_exts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


