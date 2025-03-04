# AdvisorySonatype


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_sonatype import AdvisorySonatype

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisorySonatype from a JSON string
advisory_sonatype_instance = AdvisorySonatype.from_json(json)
# print the JSON string representation of the object
print(AdvisorySonatype.to_json())

# convert the object into a dict
advisory_sonatype_dict = advisory_sonatype_instance.to_dict()
# create an instance of AdvisorySonatype from a dict
advisory_sonatype_from_dict = AdvisorySonatype.from_dict(advisory_sonatype_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


