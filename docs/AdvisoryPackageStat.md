# AdvisoryPackageStat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpe** | **str** |  | [optional] 
**fix_state** | **str** |  | [optional] 
**package_name** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_package_stat import AdvisoryPackageStat

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPackageStat from a JSON string
advisory_package_stat_instance = AdvisoryPackageStat.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPackageStat.to_json())

# convert the object into a dict
advisory_package_stat_dict = advisory_package_stat_instance.to_dict()
# create an instance of AdvisoryPackageStat from a dict
advisory_package_stat_from_dict = AdvisoryPackageStat.from_dict(advisory_package_stat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


