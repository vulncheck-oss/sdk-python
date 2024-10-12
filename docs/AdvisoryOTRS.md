# AdvisoryOTRS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**release** | **str** |  | [optional] 
**risk** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_otrs import AdvisoryOTRS

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOTRS from a JSON string
advisory_otrs_instance = AdvisoryOTRS.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOTRS.to_json())

# convert the object into a dict
advisory_otrs_dict = advisory_otrs_instance.to_dict()
# create an instance of AdvisoryOTRS from a dict
advisory_otrs_from_dict = AdvisoryOTRS.from_dict(advisory_otrs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


