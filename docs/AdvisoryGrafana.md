# AdvisoryGrafana


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_grafana import AdvisoryGrafana

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryGrafana from a JSON string
advisory_grafana_instance = AdvisoryGrafana.from_json(json)
# print the JSON string representation of the object
print(AdvisoryGrafana.to_json())

# convert the object into a dict
advisory_grafana_dict = advisory_grafana_instance.to_dict()
# create an instance of AdvisoryGrafana from a dict
advisory_grafana_from_dict = AdvisoryGrafana.from_dict(advisory_grafana_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


