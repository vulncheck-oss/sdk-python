# AdvisoryAVEVAAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aveva_vulnerability_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cwe** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**published_by** | **str** |  | [optional] 
**rating** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_aveva_advisory import AdvisoryAVEVAAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAVEVAAdvisory from a JSON string
advisory_aveva_advisory_instance = AdvisoryAVEVAAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAVEVAAdvisory.to_json())

# convert the object into a dict
advisory_aveva_advisory_dict = advisory_aveva_advisory_instance.to_dict()
# create an instance of AdvisoryAVEVAAdvisory from a dict
advisory_aveva_advisory_from_dict = AdvisoryAVEVAAdvisory.from_dict(advisory_aveva_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


