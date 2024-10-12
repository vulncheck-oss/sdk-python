# AdvisoryAdobeSolution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_adobe_solution import AdvisoryAdobeSolution

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryAdobeSolution from a JSON string
advisory_adobe_solution_instance = AdvisoryAdobeSolution.from_json(json)
# print the JSON string representation of the object
print(AdvisoryAdobeSolution.to_json())

# convert the object into a dict
advisory_adobe_solution_dict = advisory_adobe_solution_instance.to_dict()
# create an instance of AdvisoryAdobeSolution from a dict
advisory_adobe_solution_from_dict = AdvisoryAdobeSolution.from_dict(advisory_adobe_solution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


