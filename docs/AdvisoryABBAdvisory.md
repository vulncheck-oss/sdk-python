# AdvisoryABBAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abb_vulnerability_id** | **List[str]** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_abb_advisory import AdvisoryABBAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryABBAdvisory from a JSON string
advisory_abb_advisory_instance = AdvisoryABBAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryABBAdvisory.to_json())

# convert the object into a dict
advisory_abb_advisory_dict = advisory_abb_advisory_instance.to_dict()
# create an instance of AdvisoryABBAdvisory from a dict
advisory_abb_advisory_from_dict = AdvisoryABBAdvisory.from_dict(advisory_abb_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


