# AdvisoryMicrosoftDriverBlockList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_added** | **str** |  | [optional] 
**file_id** | **str** | From FileAttrib or Deny | [optional] 
**file_metadata** | [**AdvisoryMicrosoftFileMetadata**](AdvisoryMicrosoftFileMetadata.md) | File-level metadata | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_microsoft_driver_block_list import AdvisoryMicrosoftDriverBlockList

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMicrosoftDriverBlockList from a JSON string
advisory_microsoft_driver_block_list_instance = AdvisoryMicrosoftDriverBlockList.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMicrosoftDriverBlockList.to_json())

# convert the object into a dict
advisory_microsoft_driver_block_list_dict = advisory_microsoft_driver_block_list_instance.to_dict()
# create an instance of AdvisoryMicrosoftDriverBlockList from a dict
advisory_microsoft_driver_block_list_from_dict = AdvisoryMicrosoftDriverBlockList.from_dict(advisory_microsoft_driver_block_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


