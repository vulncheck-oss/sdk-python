# AdvisoryIBM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_ibm import AdvisoryIBM

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryIBM from a JSON string
advisory_ibm_instance = AdvisoryIBM.from_json(json)
# print the JSON string representation of the object
print(AdvisoryIBM.to_json())

# convert the object into a dict
advisory_ibm_dict = advisory_ibm_instance.to_dict()
# create an instance of AdvisoryIBM from a dict
advisory_ibm_from_dict = AdvisoryIBM.from_dict(advisory_ibm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


