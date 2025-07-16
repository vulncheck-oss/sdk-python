# AdvisoryNginxAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**not_vuln_versions** | **List[str]** |  | [optional] 
**patch_pgp** | **str** |  | [optional] 
**patch_url** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vuln_versions** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_nginx_advisory import AdvisoryNginxAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryNginxAdvisory from a JSON string
advisory_nginx_advisory_instance = AdvisoryNginxAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryNginxAdvisory.to_json())

# convert the object into a dict
advisory_nginx_advisory_dict = advisory_nginx_advisory_instance.to_dict()
# create an instance of AdvisoryNginxAdvisory from a dict
advisory_nginx_advisory_from_dict = AdvisoryNginxAdvisory.from_dict(advisory_nginx_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


