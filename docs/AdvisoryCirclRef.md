# AdvisoryCirclRef

advisory.CirclRef

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containers** | [**AdvisoryCirclContainers**](AdvisoryCirclContainers.md) |  | [optional] 
**cve_metadata** | [**AdvisoryCirclCveMetadata**](AdvisoryCirclCveMetadata.md) |  | [optional] 
**data_type** | **str** |  | [optional] 
**data_version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_circl_ref import AdvisoryCirclRef

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCirclRef from a JSON string
advisory_circl_ref_instance = AdvisoryCirclRef.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCirclRef.to_json())

# convert the object into a dict
advisory_circl_ref_dict = advisory_circl_ref_instance.to_dict()
# create an instance of AdvisoryCirclRef from a dict
advisory_circl_ref_from_dict = AdvisoryCirclRef.from_dict(advisory_circl_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


