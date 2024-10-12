# AdvisoryBostonScientificAdvisory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**cwe** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_boston_scientific_advisory import AdvisoryBostonScientificAdvisory

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryBostonScientificAdvisory from a JSON string
advisory_boston_scientific_advisory_instance = AdvisoryBostonScientificAdvisory.from_json(json)
# print the JSON string representation of the object
print(AdvisoryBostonScientificAdvisory.to_json())

# convert the object into a dict
advisory_boston_scientific_advisory_dict = advisory_boston_scientific_advisory_instance.to_dict()
# create an instance of AdvisoryBostonScientificAdvisory from a dict
advisory_boston_scientific_advisory_from_dict = AdvisoryBostonScientificAdvisory.from_dict(advisory_boston_scientific_advisory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


