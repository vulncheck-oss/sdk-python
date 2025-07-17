# AdvisoryCiena


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cves** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**issue_no** | **int** |  | [optional] 
**security_advisory_number** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**vulnerable_products** | [**List[AdvisoryVulnerableProduct]**](AdvisoryVulnerableProduct.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ciena import AdvisoryCiena

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCiena from a JSON string
advisory_ciena_instance = AdvisoryCiena.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCiena.to_json())

# convert the object into a dict
advisory_ciena_dict = advisory_ciena_instance.to_dict()
# create an instance of AdvisoryCiena from a dict
advisory_ciena_from_dict = AdvisoryCiena.from_dict(advisory_ciena_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


