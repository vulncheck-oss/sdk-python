# AdvisoryWolfSSL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**fixed_version** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_wolf_ssl import AdvisoryWolfSSL

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryWolfSSL from a JSON string
advisory_wolf_ssl_instance = AdvisoryWolfSSL.from_json(json)
# print the JSON string representation of the object
print(AdvisoryWolfSSL.to_json())

# convert the object into a dict
advisory_wolf_ssl_dict = advisory_wolf_ssl_instance.to_dict()
# create an instance of AdvisoryWolfSSL from a dict
advisory_wolf_ssl_from_dict = AdvisoryWolfSSL.from_dict(advisory_wolf_ssl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


