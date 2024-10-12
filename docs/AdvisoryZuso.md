# AdvisoryZuso


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**cvss** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**zaid** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_zuso import AdvisoryZuso

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryZuso from a JSON string
advisory_zuso_instance = AdvisoryZuso.from_json(json)
# print the JSON string representation of the object
print(AdvisoryZuso.to_json())

# convert the object into a dict
advisory_zuso_dict = advisory_zuso_instance.to_dict()
# create an instance of AdvisoryZuso from a dict
advisory_zuso_from_dict = AdvisoryZuso.from_dict(advisory_zuso_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


