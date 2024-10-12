# AdvisoryITW


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_itw import AdvisoryITW

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryITW from a JSON string
advisory_itw_instance = AdvisoryITW.from_json(json)
# print the JSON string representation of the object
print(AdvisoryITW.to_json())

# convert the object into a dict
advisory_itw_dict = advisory_itw_instance.to_dict()
# create an instance of AdvisoryITW from a dict
advisory_itw_from_dict = AdvisoryITW.from_dict(advisory_itw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


