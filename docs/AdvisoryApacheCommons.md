# AdvisoryApacheCommons


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_apache_commons import AdvisoryApacheCommons

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryApacheCommons from a JSON string
advisory_apache_commons_instance = AdvisoryApacheCommons.from_json(json)
# print the JSON string representation of the object
print(AdvisoryApacheCommons.to_json())

# convert the object into a dict
advisory_apache_commons_dict = advisory_apache_commons_instance.to_dict()
# create an instance of AdvisoryApacheCommons from a dict
advisory_apache_commons_from_dict = AdvisoryApacheCommons.from_dict(advisory_apache_commons_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


