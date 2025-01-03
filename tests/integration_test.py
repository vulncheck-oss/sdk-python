import os
import vulncheck_sdk
from vulncheck_sdk.api.endpoints_api import EndpointsApi
from vulncheck_sdk.api.indices_api import IndicesApi
from vulncheck_sdk.api_response import ApiResponse
from vulncheck_sdk.exceptions import ApiException, UnauthorizedException

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
    return  # TODO: revisit this
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
    for name in dir(indices_instance):
        if (
            callable(getattr(indices_instance, name))
            and name.startswith("index_nist_nvd2_get_with_http_info")
            or name.startswith("index_vulncheck_kev_get_with_http_info")
            or name.startswith("index_ipintel3d_get_with_http_info")
            or name.startswith("index_cisa_kev_get_with_http_info")
        ):
            method = getattr(indices_instance, name)
            print(name)
            status = _get_http_status(method, 1, 1)
            assert status == 200


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
        return api_response.status_code


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
