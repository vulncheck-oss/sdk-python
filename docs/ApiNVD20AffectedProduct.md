# ApiNVD20AffectedProduct

api.NVD20AffectedProduct

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_url** | **str** |  | [optional] 
**cpes** | **List[str]** |  | [optional] 
**default_status** | **str** | DefaultStatus is the status for versions not otherwise listed: one of \&quot;affected\&quot;, \&quot;unaffected\&quot;, or \&quot;unknown\&quot;. | [optional] 
**modules** | **List[str]** |  | [optional] 
**package_name** | **str** |  | [optional] 
**package_url** | **str** |  | [optional] 
**platforms** | **List[str]** |  | [optional] 
**product** | **str** |  | [optional] 
**program_files** | **List[str]** |  | [optional] 
**program_routines** | [**List[ApiNVD20AffectedProgramRoutine]**](ApiNVD20AffectedProgramRoutine.md) |  | [optional] 
**repo** | **str** |  | [optional] 
**vendor** | **str** |  | [optional] 
**versions** | [**List[ApiNVD20AffectedVersion]**](ApiNVD20AffectedVersion.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.api_nvd20_affected_product import ApiNVD20AffectedProduct

# TODO update the JSON string below
json = "{}"
# create an instance of ApiNVD20AffectedProduct from a JSON string
api_nvd20_affected_product_instance = ApiNVD20AffectedProduct.from_json(json)
# print the JSON string representation of the object
print(ApiNVD20AffectedProduct.to_json())

# convert the object into a dict
api_nvd20_affected_product_dict = api_nvd20_affected_product_instance.to_dict()
# create an instance of ApiNVD20AffectedProduct from a dict
api_nvd20_affected_product_from_dict = ApiNVD20AffectedProduct.from_dict(api_nvd20_affected_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


