# AdvisorySalesForce


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**link** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_sales_force import AdvisorySalesForce

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySalesForce from a JSON string
advisory_sales_force_instance = AdvisorySalesForce.from_json(json)
# print the JSON string representation of the object
print(AdvisorySalesForce.to_json())

# convert the object into a dict
advisory_sales_force_dict = advisory_sales_force_instance.to_dict()
# create an instance of AdvisorySalesForce from a dict
advisory_sales_force_from_dict = AdvisorySalesForce.from_dict(advisory_sales_force_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


