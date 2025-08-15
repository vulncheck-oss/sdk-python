# AdvisoryCrowdSec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**eitw** | **bool** |  | [optional] 
**first_seen** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_crowd_sec import AdvisoryCrowdSec

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCrowdSec from a JSON string
advisory_crowd_sec_instance = AdvisoryCrowdSec.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCrowdSec.to_json())

# convert the object into a dict
advisory_crowd_sec_dict = advisory_crowd_sec_instance.to_dict()
# create an instance of AdvisoryCrowdSec from a dict
advisory_crowd_sec_from_dict = AdvisoryCrowdSec.from_dict(advisory_crowd_sec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


