# AdvisoryApacheHTTP


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_apache_http import AdvisoryApacheHTTP

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryApacheHTTP from a JSON string
advisory_apache_http_instance = AdvisoryApacheHTTP.from_json(json)
# print the JSON string representation of the object
print(AdvisoryApacheHTTP.to_json())

# convert the object into a dict
advisory_apache_http_dict = advisory_apache_http_instance.to_dict()
# create an instance of AdvisoryApacheHTTP from a dict
advisory_apache_http_from_dict = AdvisoryApacheHTTP.from_dict(advisory_apache_http_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


