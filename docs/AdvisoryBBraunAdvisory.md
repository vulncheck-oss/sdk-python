# AdvisoryBBraunAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attention** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cwe** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**equipment** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 
**vulnerabilities** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_b_braun_advisory import AdvisoryBBraunAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBBraunAdvisory from a JSON string
advisory_b_braun_advisory_instance = AdvisoryBBraunAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBBraunAdvisory.to_json())

# convert the object into a dict
advisory_b_braun_advisory_dict = advisory_b_braun_advisory_instance.to_dict()
# create an instance of AdvisoryBBraunAdvisory from a dict
advisory_b_braun_advisory_from_dict = AdvisoryBBraunAdvisory.from_dict(advisory_b_braun_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


