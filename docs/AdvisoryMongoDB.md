# AdvisoryMongoDB


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**score** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_mongo_db import AdvisoryMongoDB

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryMongoDB from a JSON string
advisory_mongo_db_instance = AdvisoryMongoDB.from_json(json)
# print the JSON string representation of the object
print(AdvisoryMongoDB.to_json())

# convert the object into a dict
advisory_mongo_db_dict = advisory_mongo_db_instance.to_dict()
# create an instance of AdvisoryMongoDB from a dict
advisory_mongo_db_from_dict = AdvisoryMongoDB.from_dict(advisory_mongo_db_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


