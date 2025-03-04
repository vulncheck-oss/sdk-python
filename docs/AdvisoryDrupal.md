# AdvisoryDrupal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**project** | **str** |  | [optional] 
**risk** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_drupal import AdvisoryDrupal

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryDrupal from a JSON string
advisory_drupal_instance = AdvisoryDrupal.from_json(json)
# print the JSON string representation of the object
print(AdvisoryDrupal.to_json())

# convert the object into a dict
advisory_drupal_dict = advisory_drupal_instance.to_dict()
# create an instance of AdvisoryDrupal from a dict
advisory_drupal_from_dict = AdvisoryDrupal.from_dict(advisory_drupal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


