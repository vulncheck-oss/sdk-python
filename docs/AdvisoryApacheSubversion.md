# AdvisoryApacheSubversion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_apache_subversion import AdvisoryApacheSubversion

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryApacheSubversion from a JSON string
advisory_apache_subversion_instance = AdvisoryApacheSubversion.from_json(json)
# print the JSON string representation of the object
print(AdvisoryApacheSubversion.to_json())

# convert the object into a dict
advisory_apache_subversion_dict = advisory_apache_subversion_instance.to_dict()
# create an instance of AdvisoryApacheSubversion from a dict
advisory_apache_subversion_from_dict = AdvisoryApacheSubversion.from_dict(advisory_apache_subversion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


