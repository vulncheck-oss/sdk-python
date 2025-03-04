# AdvisorySevenZip


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_seven_zip import AdvisorySevenZip

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySevenZip from a JSON string
advisory_seven_zip_instance = AdvisorySevenZip.from_json(json)
# print the JSON string representation of the object
print(AdvisorySevenZip.to_json())

# convert the object into a dict
advisory_seven_zip_dict = advisory_seven_zip_instance.to_dict()
# create an instance of AdvisorySevenZip from a dict
advisory_seven_zip_from_dict = AdvisorySevenZip.from_dict(advisory_seven_zip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


