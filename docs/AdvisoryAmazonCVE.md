# AdvisoryAmazonCVE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | [**List[AdvisoryAmazonAffectedPackage]**](AdvisoryAmazonAffectedPackage.md) |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**cvss_score** | **str** |  | [optional] 
**cvss_vector** | **str** |  | [optional] 
**date_added** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_amazon_cve import AdvisoryAmazonCVE

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAmazonCVE from a JSON string
advisory_amazon_cve_instance = AdvisoryAmazonCVE.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAmazonCVE.to_json())

# convert the object into a dict
advisory_amazon_cve_dict = advisory_amazon_cve_instance.to_dict()
# create an instance of AdvisoryAmazonCVE from a dict
advisory_amazon_cve_from_dict = AdvisoryAmazonCVE.from_dict(advisory_amazon_cve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


