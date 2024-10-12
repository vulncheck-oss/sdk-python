# AdvisoryApacheOpenOffice


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
from vulncheck_sdk.models.advisory_apache_open_office import AdvisoryApacheOpenOffice

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryApacheOpenOffice from a JSON string
advisory_apache_open_office_instance = AdvisoryApacheOpenOffice.from_json(json)
# print the JSON string representation of the object
print(AdvisoryApacheOpenOffice.to_json())

# convert the object into a dict
advisory_apache_open_office_dict = advisory_apache_open_office_instance.to_dict()
# create an instance of AdvisoryApacheOpenOffice from a dict
advisory_apache_open_office_from_dict = AdvisoryApacheOpenOffice.from_dict(advisory_apache_open_office_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


