# AdvisoryFortinetIPS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affected** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**epss** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**references** | **List[str]** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_fortinet_ips import AdvisoryFortinetIPS

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryFortinetIPS from a JSON string
advisory_fortinet_ips_instance = AdvisoryFortinetIPS.from_json(json)
# print the JSON string representation of the object
print(AdvisoryFortinetIPS.to_json())

# convert the object into a dict
advisory_fortinet_ips_dict = advisory_fortinet_ips_instance.to_dict()
# create an instance of AdvisoryFortinetIPS from a dict
advisory_fortinet_ips_from_dict = AdvisoryFortinetIPS.from_dict(advisory_fortinet_ips_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


