# import requests
import os
import vulncheck_sdk
from vulncheck_sdk.api.endpoints_api import EndpointsApi
from vulncheck_sdk.api.indices_api import IndicesApi
from vulncheck_sdk.api_response import ApiResponse
from vulncheck_sdk.exceptions import ApiException, UnauthorizedException
from vulncheck_sdk.models.paginate_pagination import PaginatePagination
from vulncheck_sdk.models.params_idx_req_params import ParamsIdxReqParams
from vulncheck_sdk.models.v3controllers_purl_response_data import (
    V3controllersPurlResponseData,
)

DEFAULT_HOST = "https://api.vulncheck.com"
DEFAULT_API = DEFAULT_HOST + "/v3"
API_TOKEN = os.environ["VULNCHECK_API_TOKEN"]

"""
ApiEndpoint Tests
"""


def test_openapi_get():
    api_instance = _get_api_instance()
    status = _get_http_status(api_instance.openapi_get_with_http_info)
    assert status == 200


def test_entitlements_get():
    api_instance = _get_api_instance(API_TOKEN)
    status = _get_http_status(api_instance.entitlements_get_with_http_info)
    assert status == 200


def test_purl_get():
    api_instance = _get_api_instance(API_TOKEN)
    status = _get_http_status(
        api_instance.purl_get_with_http_info, "pkg:hex/coherence@0.1.2"
    )
    assert status == 200


def test_index_get():
    api_instance = _get_api_instance(API_TOKEN)
    status = _get_http_status(api_instance.index_get_with_http_info)
    assert status == 200


def test_cpe_get():
    api_instance = _get_api_instance(API_TOKEN)
    status = _get_http_status(
        api_instance.cpe_get_with_http_info,
        "cpe:/a:microsoft:internet_explorer:8.0.6001:beta",
    )
    assert status == 200


def test_backup_get():
    api_instance = _get_api_instance(API_TOKEN)
    status = _get_http_status(api_instance.backup_get_with_http_info)
    assert status == 200


def test_backup_index_get():
    api_instance = _get_api_instance(API_TOKEN)
    status = _get_http_status(api_instance.backup_index_get_with_http_info, "")
    assert status == 200


def test_pdns_vulncheck_c2_get():
    api_instance = _get_api_instance(API_TOKEN)
    status = _get_http_status(api_instance.pdns_vulncheck_c2_get_with_http_info, "")
    assert status == 200


def test_tags_vulncheck_c2_get():
    api_instance = _get_api_instance(API_TOKEN)
    status = _get_http_status(api_instance.tags_vulncheck_c2_get_with_http_info, "")
    assert status == 200


def test_rules_initial_access_type_get():
    api_instance = _get_api_instance(API_TOKEN)
    status = _get_http_status(
        api_instance.rules_initial_access_type_get_with_http_info, "suricata"
    )
    assert status == 200


"""
IndicesApi Tests
"""


def test_all_indicies():
    indices_instance = _get_indices_instance(API_TOKEN)
    params = ParamsIdxReqParams()
    for name in dir(indices_instance):
        if (
            callable(getattr(indices_instance, name))
            and name.startswith("index_")
            and name.endswith("_get_with_http_info")
            and not name.startswith("index_npm_get")  # HACK: timeout issues
            and not name.startswith("index_initial_access_git_get")
        ):
            method = getattr(indices_instance, name)
            print(name)
            status = _get_http_status(method, params, 1, 1)
            assert status == 200


# def test_example_purl():
#     endpoints_client = _get_api_instance(API_TOKEN)
#     purl = "pkg:hex/coherence@0.1.2"
#     api_response = endpoints_client.purl_get(purl)
#     if api_response.data is not None:
#         data: V3controllersPurlResponseData = api_response.data
#         print(data.cves)
#
#
# def test_example_cpe():
#     endpoints_client = _get_api_instance(API_TOKEN)
#     cpe = "cpe:/a:microsoft:internet_explorer:8.0.6001:beta"
#     api_response = endpoints_client.cpe_get(cpe)
#     if api_response.data is not None:
#         for cve in api_response.data:
#             print(cve)
#
#
# def test_example_indicies():
#     endpoints_client = _get_api_instance(API_TOKEN)
#     api_response = endpoints_client.index_get()
#     if api_response.data is not None:
#         for index in api_response.data:
#             print(index.name)
#
#
# def test_example_backup():
#     endpoints_client = _get_api_instance(API_TOKEN)
#     index = "initial-access"
#     api_response = endpoints_client.backup_index_get(index)
#     backup_url = requests.get(api_response.data[0].url)
#     if backup_url.status_code == 200:
#         file_path = f"{index}.zip"
#
#         with open(file_path, "wb") as file:
#             file.write(backup_url.content)
#
#         print(f"File downloaded successfully and saved as {file_path}")
#     else:
#         print(f"Failed to download the file. Status code: {backup_url.status_code}")
#
#
# def test_example_pagination():
#     indices_instance = _get_indices_instance(API_TOKEN)
#     query_params = vulncheck_sdk.ParamsIdxReqParams()
#     limit = 10
#     page = 1
#     while page <= 5:
#         api_response = indices_instance.index_ipintel3d_get(
#             query_params, limit=limit, page=page
#         )
#         print(f"Page {page}:")
#         print(api_response.data)
#
#         meta: PaginatePagination = api_response.meta
#         if meta.page >= meta.total_pages:
#             break
#         page += 1


"""
Helpers
"""


def _get_http_status(func, params=None, limit=None, page=None) -> int:
    api_response = ApiResponse
    try:
        if params is None:
            api_response = func()
        elif limit is None or page is None:
            api_response = func(params)
        else:
            api_response = func(params, limit, page)
        return api_response.status_code
    except UnauthorizedException as e:
        print("Not authorized for this endpoint: %s\n" % e)
        return 401
    except ApiException as e:
        print(f"ApiException when calling {func}: {e}\n")
        return api_response.status_code if api_response else 0


def _get_api_instance(token: str = "") -> EndpointsApi:
    config = vulncheck_sdk.Configuration(host=DEFAULT_API)
    if token != "":
        config.api_key["Bearer"] = token
    client = vulncheck_sdk.ApiClient(config)
    return vulncheck_sdk.EndpointsApi(client)


def _get_indices_instance(token: str = "") -> IndicesApi:
    config = vulncheck_sdk.Configuration(host=DEFAULT_API)
    if token != "":
        config.api_key["Bearer"] = token
    client = vulncheck_sdk.ApiClient(config)
    return vulncheck_sdk.IndicesApi(client)
