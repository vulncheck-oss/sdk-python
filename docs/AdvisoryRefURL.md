# AdvisoryRefURL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_added** | **str** |  | [optional] 
**exploit_availability** | **str** |  | [optional] 
**exploit_maturity** | **str** |  | [optional] 
**lang** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ref_url import AdvisoryRefURL

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRefURL from a JSON string
advisory_ref_url_instance = AdvisoryRefURL.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRefURL.to_json())

# convert the object into a dict
advisory_ref_url_dict = advisory_ref_url_instance.to_dict()
# create an instance of AdvisoryRefURL from a dict
advisory_ref_url_from_dict = AdvisoryRefURL.from_dict(advisory_ref_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


