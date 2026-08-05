# AdvisoryCVDSnapshot

Snapshot provenance — which payload.json snapshot this record came from. ManifestSHA3 + Revision + AsOf are stable per-snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_of** | **str** |  | [optional] 
**fetched_at** | **str** |  | [optional] 
**manifest_sha3** | **str** |  | [optional] 
**revision** | **int** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.advisory_cvd_snapshot import AdvisoryCVDSnapshot

# TODO update the JSON string below
json = "{}"
# create an instance of AdvisoryCVDSnapshot from a JSON string
advisory_cvd_snapshot_instance = AdvisoryCVDSnapshot.from_json(json)
# print the JSON string representation of the object
print(AdvisoryCVDSnapshot.to_json())

# convert the object into a dict
advisory_cvd_snapshot_dict = advisory_cvd_snapshot_instance.to_dict()
# create an instance of AdvisoryCVDSnapshot from a dict
advisory_cvd_snapshot_from_dict = AdvisoryCVDSnapshot.from_dict(advisory_cvd_snapshot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


