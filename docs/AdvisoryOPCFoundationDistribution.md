# AdvisoryOPCFoundationDistribution

advisory.OPCFoundationDistribution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tlp** | [**AdvisoryOPCFoundationTLP**](AdvisoryOPCFoundationTLP.md) |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_opc_foundation_distribution import AdvisoryOPCFoundationDistribution

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOPCFoundationDistribution from a JSON string
advisory_opc_foundation_distribution_instance = AdvisoryOPCFoundationDistribution.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOPCFoundationDistribution.to_json())

# convert the object into a dict
advisory_opc_foundation_distribution_dict = advisory_opc_foundation_distribution_instance.to_dict()
# create an instance of AdvisoryOPCFoundationDistribution from a dict
advisory_opc_foundation_distribution_from_dict = AdvisoryOPCFoundationDistribution.from_dict(advisory_opc_foundation_distribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


