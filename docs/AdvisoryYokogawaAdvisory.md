# AdvisoryYokogawaAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**cwe** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**date_last_revised** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**ysar_id** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_yokogawa_advisory import AdvisoryYokogawaAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryYokogawaAdvisory from a JSON string
advisory_yokogawa_advisory_instance = AdvisoryYokogawaAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryYokogawaAdvisory.to_json())

# convert the object into a dict
advisory_yokogawa_advisory_dict = advisory_yokogawa_advisory_instance.to_dict()
# create an instance of AdvisoryYokogawaAdvisory from a dict
advisory_yokogawa_advisory_from_dict = AdvisoryYokogawaAdvisory.from_dict(advisory_yokogawa_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


