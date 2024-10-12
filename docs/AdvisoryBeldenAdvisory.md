# AdvisoryBeldenAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**belden_id** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cwe** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**date_last_updated** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_belden_advisory import AdvisoryBeldenAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBeldenAdvisory from a JSON string
advisory_belden_advisory_instance = AdvisoryBeldenAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBeldenAdvisory.to_json())

# convert the object into a dict
advisory_belden_advisory_dict = advisory_belden_advisory_instance.to_dict()
# create an instance of AdvisoryBeldenAdvisory from a dict
advisory_belden_advisory_from_dict = AdvisoryBeldenAdvisory.from_dict(advisory_belden_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


