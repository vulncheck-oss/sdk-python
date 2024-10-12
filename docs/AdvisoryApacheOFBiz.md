# AdvisoryApacheOFBiz


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**fixed** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_apache_of_biz import AdvisoryApacheOFBiz

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryApacheOFBiz from a JSON string
advisory_apache_of_biz_instance = AdvisoryApacheOFBiz.from_json(json)
# print the JSON string representation of the object
print(AdvisoryApacheOFBiz.to_json())

# convert the object into a dict
advisory_apache_of_biz_dict = advisory_apache_of_biz_instance.to_dict()
# create an instance of AdvisoryApacheOFBiz from a dict
advisory_apache_of_biz_from_dict = AdvisoryApacheOFBiz.from_dict(advisory_apache_of_biz_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


