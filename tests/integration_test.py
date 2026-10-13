import os
import vulncheck_sdk
from vulncheck_sdk.api.endpoints_api import EndpointsApi
from vulncheck_sdk.api.indices_api import IndicesApi
from vulncheck_sdk.api.nvd_api import NvdApi
from vulncheck_sdk.api_response import ApiResponse
from vulncheck_sdk.exceptions import ApiException, UnauthorizedException

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
    status = _get_http_status(api_instance.backup_index_get_with_http_info, "initial-access")
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
NvdApi Tests
"""

NVD_CVE_ID = "CVE-2021-44228"


def test_nvd_cves_get():
    response = _get_nvd_instance(API_TOKEN).nvd_cves_get(cve_id=NVD_CVE_ID)
    assert response.total_results == 1
    assert response.vulnerabilities[0].cve.id == NVD_CVE_ID


def test_nvd_cves_get_cursor():
    nvd = _get_nvd_instance(API_TOKEN)
    first = nvd.nvd_cves_get(cve_tag="disputed", results_per_page=5, cursor="")
    assert first.next_cursor
    second = nvd.nvd_cves_get(cve_tag="disputed", results_per_page=5, cursor=first.next_cursor)
    assert second.vulnerabilities[0].cve.id != first.vulnerabilities[0].cve.id


def test_nvd_cve_history_get():
    response = _get_nvd_instance(API_TOKEN).nvd_cve_history_get(cve_id=NVD_CVE_ID)
    assert response.cve_changes


def test_nvd_cpes_get():
    response = _get_nvd_instance(API_TOKEN).nvd_cpes_get(
        cpe_match_string="cpe:2.3:a:apache:log4j", results_per_page=5
    )
    assert response.products


def test_nvd_cpe_match_get():
    response = _get_nvd_instance(API_TOKEN).nvd_cpe_match_get(cve_id=NVD_CVE_ID, results_per_page=5)
    assert response.match_strings


def test_nvd_source_get():
    response = _get_nvd_instance(API_TOKEN).nvd_source_get(results_per_page=5)
    assert response.sources


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
        return e.status


def _get_api_instance(token: str = "") -> EndpointsApi:
    config = vulncheck_sdk.Configuration()
    if token != "":
        config.api_key["Bearer"] = token
    client = vulncheck_sdk.ApiClient(config)
    return vulncheck_sdk.EndpointsApi(client)


def _get_indices_instance(token: str = "") -> IndicesApi:
    config = vulncheck_sdk.Configuration()
    if token != "":
        config.api_key["Bearer"] = token
    client = vulncheck_sdk.ApiClient(config)
    return vulncheck_sdk.IndicesApi(client)


def _get_nvd_instance(token: str = "") -> NvdApi:
    config = vulncheck_sdk.Configuration()
    if token != "":
        config.api_key["Bearer"] = token
    client = vulncheck_sdk.ApiClient(config)
    return vulncheck_sdk.NvdApi(client)
