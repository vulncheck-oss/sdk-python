# AdvisoryApacheArchiva


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_apache_archiva import AdvisoryApacheArchiva

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryApacheArchiva from a JSON string
advisory_apache_archiva_instance = AdvisoryApacheArchiva.from_json(json)
# print the JSON string representation of the object
print(AdvisoryApacheArchiva.to_json())

# convert the object into a dict
advisory_apache_archiva_dict = advisory_apache_archiva_instance.to_dict()
# create an instance of AdvisoryApacheArchiva from a dict
advisory_apache_archiva_from_dict = AdvisoryApacheArchiva.from_dict(advisory_apache_archiva_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


