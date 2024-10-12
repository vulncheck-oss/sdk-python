# AdvisoryApacheSuperset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_apache_superset import AdvisoryApacheSuperset

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryApacheSuperset from a JSON string
advisory_apache_superset_instance = AdvisoryApacheSuperset.from_json(json)
# print the JSON string representation of the object
print(AdvisoryApacheSuperset.to_json())

# convert the object into a dict
advisory_apache_superset_dict = advisory_apache_superset_instance.to_dict()
# create an instance of AdvisoryApacheSuperset from a dict
advisory_apache_superset_from_dict = AdvisoryApacheSuperset.from_dict(advisory_apache_superset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


