# AdvisoryApacheShiro


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_apache_shiro import AdvisoryApacheShiro

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryApacheShiro from a JSON string
advisory_apache_shiro_instance = AdvisoryApacheShiro.from_json(json)
# print the JSON string representation of the object
print(AdvisoryApacheShiro.to_json())

# convert the object into a dict
advisory_apache_shiro_dict = advisory_apache_shiro_instance.to_dict()
# create an instance of AdvisoryApacheShiro from a dict
advisory_apache_shiro_from_dict = AdvisoryApacheShiro.from_dict(advisory_apache_shiro_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


