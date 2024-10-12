# AdvisoryOracleCPU


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_oracle_cpu import AdvisoryOracleCPU

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOracleCPU from a JSON string
advisory_oracle_cpu_instance = AdvisoryOracleCPU.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOracleCPU.to_json())

# convert the object into a dict
advisory_oracle_cpu_dict = advisory_oracle_cpu_instance.to_dict()
# create an instance of AdvisoryOracleCPU from a dict
advisory_oracle_cpu_from_dict = AdvisoryOracleCPU.from_dict(advisory_oracle_cpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


