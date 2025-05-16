# AdvisoryEUVD


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | **List[str]** |  | [optional] 
**assigner** | **str** |  | [optional] 
**base_score** | **float** |  | [optional] 
**base_score_vector** | **str** |  | [optional] 
**base_score_version** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**date_updated** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enisa_id_product** | [**List[AdvisoryEnisaIDProduct]**](AdvisoryEnisaIDProduct.md) |  | [optional] 
**enisa_id_vendor** | [**List[AdvisoryEnisaIDVendor]**](AdvisoryEnisaIDVendor.md) |  | [optional] 
**epss** | **float** |  | [optional] 
**exploited** | **bool** | This field is exploited field from endpoint /api/vulnerabilities. apidocs : https://euvd.enisa.europa.eu/apidoc Note: There are records where exploited_since is populated with a valid date, but it still shows up under non_exploitable data set | [optional] 
**exploited_since** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_euvd import AdvisoryEUVD

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryEUVD from a JSON string
advisory_euvd_instance = AdvisoryEUVD.from_json(json)
# print the JSON string representation of the object
print(AdvisoryEUVD.to_json())

# convert the object into a dict
advisory_euvd_dict = advisory_euvd_instance.to_dict()
# create an instance of AdvisoryEUVD from a dict
advisory_euvd_from_dict = AdvisoryEUVD.from_dict(advisory_euvd_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


