# RenderNvdErrorBody

render.NvdErrorBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**status** | **int** |  | [optional] 

## Example

```python
from vulncheck_sdk.models.render_nvd_error_body import RenderNvdErrorBody

# TODO update the JSON string below
json = "{}"
# create an instance of RenderNvdErrorBody from a JSON string
render_nvd_error_body_instance = RenderNvdErrorBody.from_json(json)
# print the JSON string representation of the object
print(RenderNvdErrorBody.to_json())

# convert the object into a dict
render_nvd_error_body_dict = render_nvd_error_body_instance.to_dict()
# create an instance of RenderNvdErrorBody from a dict
render_nvd_error_body_from_dict = RenderNvdErrorBody.from_dict(render_nvd_error_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


