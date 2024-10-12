# AdvisoryAzul


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_score** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**prime_version** | [**List[AdvisoryPrimeVersion]**](AdvisoryPrimeVersion.md) |  | [optional] 
**release** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**zulu_version** | [**List[AdvisoryZuluVersion]**](AdvisoryZuluVersion.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_azul import AdvisoryAzul

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAzul from a JSON string
advisory_azul_instance = AdvisoryAzul.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAzul.to_json())

# convert the object into a dict
advisory_azul_dict = advisory_azul_instance.to_dict()
# create an instance of AdvisoryAzul from a dict
advisory_azul_from_dict = AdvisoryAzul.from_dict(advisory_azul_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


