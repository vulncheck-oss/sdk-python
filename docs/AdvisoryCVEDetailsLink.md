# AdvisoryCVEDetailsLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cve_details_link import AdvisoryCVEDetailsLink

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCVEDetailsLink from a JSON string
advisory_cve_details_link_instance = AdvisoryCVEDetailsLink.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCVEDetailsLink.to_json())

# convert the object into a dict
advisory_cve_details_link_dict = advisory_cve_details_link_instance.to_dict()
# create an instance of AdvisoryCVEDetailsLink from a dict
advisory_cve_details_link_from_dict = AdvisoryCVEDetailsLink.from_dict(advisory_cve_details_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


