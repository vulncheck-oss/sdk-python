# AdvisoryRockyErrata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advisory** | [**AdvisoryRockyAdvisory**](AdvisoryRockyAdvisory.md) |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**packages** | [**List[AdvisoryRockyPackage]**](AdvisoryRockyPackage.md) |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_rocky_errata import AdvisoryRockyErrata

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryRockyErrata from a JSON string
advisory_rocky_errata_instance = AdvisoryRockyErrata.from_json(json)
# print the JSON string representation of the object
print(AdvisoryRockyErrata.to_json())

# convert the object into a dict
advisory_rocky_errata_dict = advisory_rocky_errata_instance.to_dict()
# create an instance of AdvisoryRockyErrata from a dict
advisory_rocky_errata_from_dict = AdvisoryRockyErrata.from_dict(advisory_rocky_errata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


