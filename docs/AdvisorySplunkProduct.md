# AdvisorySplunkProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected_version** | **str** |  | [optional] 
**component** | **str** |  | [optional] 
**fixed_version** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_splunk_product import AdvisorySplunkProduct

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySplunkProduct from a JSON string
advisory_splunk_product_instance = AdvisorySplunkProduct.from_json(json)
# print the JSON string representation of the object
print(AdvisorySplunkProduct.to_json())

# convert the object into a dict
advisory_splunk_product_dict = advisory_splunk_product_instance.to_dict()
# create an instance of AdvisorySplunkProduct from a dict
advisory_splunk_product_from_dict = AdvisorySplunkProduct.from_dict(advisory_splunk_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


