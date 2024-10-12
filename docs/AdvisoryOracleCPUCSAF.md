# AdvisoryOracleCPUCSAF


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csaf** | [**AdvisoryCSAF**](AdvisoryCSAF.md) |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_oracle_cpucsaf import AdvisoryOracleCPUCSAF

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOracleCPUCSAF from a JSON string
advisory_oracle_cpucsaf_instance = AdvisoryOracleCPUCSAF.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOracleCPUCSAF.to_json())

# convert the object into a dict
advisory_oracle_cpucsaf_dict = advisory_oracle_cpucsaf_instance.to_dict()
# create an instance of AdvisoryOracleCPUCSAF from a dict
advisory_oracle_cpucsaf_from_dict = AdvisoryOracleCPUCSAF.from_dict(advisory_oracle_cpucsaf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


