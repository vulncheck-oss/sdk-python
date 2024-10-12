# AdvisoryPostgresSQL


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cve** | **List[str]** |  | [optional] 
**date_added** | **str** |  | [optional] 
**pg_fix** | [**List[AdvisoryPGFix]**](AdvisoryPGFix.md) |  | [optional] 
**summary** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_postgres_sql import AdvisoryPostgresSQL

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryPostgresSQL from a JSON string
advisory_postgres_sql_instance = AdvisoryPostgresSQL.from_json(json)
# print the JSON string representation of the object
print(AdvisoryPostgresSQL.to_json())

# convert the object into a dict
advisory_postgres_sql_dict = advisory_postgres_sql_instance.to_dict()
# create an instance of AdvisoryPostgresSQL from a dict
advisory_postgres_sql_from_dict = AdvisoryPostgresSQL.from_dict(advisory_postgres_sql_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


