# ApiCveItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configurations** | [**ApiConfigurations**](ApiConfigurations.md) |  | [optional] 
**cve** | [**ApiCVE**](ApiCVE.md) |  | [optional] 
**impact** | [**ApiImpact**](ApiImpact.md) |  | [optional] 
**last_modified_date** | **str** |  | [optional] 
**published_date** | **str** |  | [optional] 
**vc_configurations** | [**ApiConfigurations**](ApiConfigurations.md) |  | [optional] 
**vc_vulnerable_cpes** | **List[str]** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_cve_items import ApiCveItems

# TODO update the JSON string below
json = "{}"
# create an instance of ApiCveItems from a JSON string
api_cve_items_instance = ApiCveItems.from_json(json)
# print the JSON string representation of the object
print(ApiCveItems.to_json())

# convert the object into a dict
api_cve_items_dict = api_cve_items_instance.to_dict()
# create an instance of ApiCveItems from a dict
api_cve_items_from_dict = ApiCveItems.from_dict(api_cve_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


