# AdvisoryAsterisk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_asterisk import AdvisoryAsterisk

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAsterisk from a JSON string
advisory_asterisk_instance = AdvisoryAsterisk.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAsterisk.to_json())

# convert the object into a dict
advisory_asterisk_dict = advisory_asterisk_instance.to_dict()
# create an instance of AdvisoryAsterisk from a dict
advisory_asterisk_from_dict = AdvisoryAsterisk.from_dict(advisory_asterisk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


