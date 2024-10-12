# AdvisorySiemensDistribution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**tlp** | [**AdvisorySiemensTLP**](AdvisorySiemensTLP.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_siemens_distribution import AdvisorySiemensDistribution

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySiemensDistribution from a JSON string
advisory_siemens_distribution_instance = AdvisorySiemensDistribution.from_json(json)
# print the JSON string representation of the object
print(AdvisorySiemensDistribution.to_json())

# convert the object into a dict
advisory_siemens_distribution_dict = advisory_siemens_distribution_instance.to_dict()
# create an instance of AdvisorySiemensDistribution from a dict
advisory_siemens_distribution_from_dict = AdvisorySiemensDistribution.from_dict(advisory_siemens_distribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


