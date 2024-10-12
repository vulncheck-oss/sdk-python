# AdvisoryOSVReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_osv_reference import AdvisoryOSVReference

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryOSVReference from a JSON string
advisory_osv_reference_instance = AdvisoryOSVReference.from_json(json)
# print the JSON string representation of the object
print(AdvisoryOSVReference.to_json())

# convert the object into a dict
advisory_osv_reference_dict = advisory_osv_reference_instance.to_dict()
# create an instance of AdvisoryOSVReference from a dict
advisory_osv_reference_from_dict = AdvisoryOSVReference.from_dict(advisory_osv_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


