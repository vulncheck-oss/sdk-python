# AdvisoryApacheGuacamole


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
from vulncheck_sdk.models.advisory_apache_guacamole import AdvisoryApacheGuacamole

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryApacheGuacamole from a JSON string
advisory_apache_guacamole_instance = AdvisoryApacheGuacamole.from_json(json)
# print the JSON string representation of the object
print(AdvisoryApacheGuacamole.to_json())

# convert the object into a dict
advisory_apache_guacamole_dict = advisory_apache_guacamole_instance.to_dict()
# create an instance of AdvisoryApacheGuacamole from a dict
advisory_apache_guacamole_from_dict = AdvisoryApacheGuacamole.from_dict(advisory_apache_guacamole_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


