# AdvisoryAmazonAffectedPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory** | **str** |  | [optional] 
**package** | **str** |  | [optional] 
**platform** | **str** |  | [optional] 
**release_date** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_amazon_affected_package import AdvisoryAmazonAffectedPackage

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAmazonAffectedPackage from a JSON string
advisory_amazon_affected_package_instance = AdvisoryAmazonAffectedPackage.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAmazonAffectedPackage.to_json())

# convert the object into a dict
advisory_amazon_affected_package_dict = advisory_amazon_affected_package_instance.to_dict()
# create an instance of AdvisoryAmazonAffectedPackage from a dict
advisory_amazon_affected_package_from_dict = AdvisoryAmazonAffectedPackage.from_dict(advisory_amazon_affected_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


