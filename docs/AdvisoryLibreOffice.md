# AdvisoryLibreOffice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_libre_office import AdvisoryLibreOffice

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryLibreOffice from a JSON string
advisory_libre_office_instance = AdvisoryLibreOffice.from_json(json)
# print the JSON string representation of the object
print(AdvisoryLibreOffice.to_json())

# convert the object into a dict
advisory_libre_office_dict = advisory_libre_office_instance.to_dict()
# create an instance of AdvisoryLibreOffice from a dict
advisory_libre_office_from_dict = AdvisoryLibreOffice.from_dict(advisory_libre_office_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


