import os
import asyncio
import vulncheck_sdk.aio as vcaio
from vulncheck_sdk.aio.api.endpoints_api import EndpointsApi
from vulncheck_sdk.aio.api.indices_api import IndicesApi
from vulncheck_sdk.aio.api.nvd_api import NvdApi
from vulncheck_sdk.aio.exceptions import ApiException, UnauthorizedException

API_TOKEN = os.environ.get("VULNCHECK_API_TOKEN", "")

# --- Helpers ---


async def _get_http_status(func, *args) -> int:
    """Awaits the SDK call and returns the status code, handling common exceptions."""
    try:
        api_response = await func(*args)
        return api_response.status_code
    except UnauthorizedException as e:
        print(f"Not authorized for this endpoint: {e}")
        return 401
    except ApiException as e:
        status = getattr(e, "status", 500)
        print(f"ApiException (Status {status}) when calling {func.__name__}: {e}")
        return status
    except Exception as e:
        print(f"Unexpected error in {func.__name__}: {e}")
        return 500


# --- EndpointsApi Tests ---


async def _check_openapi_get(api: EndpointsApi) -> None:
    print(f"Testing test_openapi_get")
    status = await _get_http_status(api.openapi_get_with_http_info)
    assert status == 200


async def _check_entitlements_get(api: EndpointsApi) -> None:
    print(f"Testing test_entitlements_get")
    status = await _get_http_status(api.entitlements_get_with_http_info)
    assert status == 200


async def _check_purl_get(api: EndpointsApi) -> None:
    print(f"Testing test_purl_get")
    status = await _get_http_status(
        api.purl_get_with_http_info, "pkg:hex/coherence@0.1.2"
    )
    assert status == 200


async def _check_index_get(api: EndpointsApi) -> None:
    print(f"Testing test_index_get")
    status = await _get_http_status(api.index_get_with_http_info)
    assert status == 200


async def _check_cpe_get(api: EndpointsApi) -> None:
    print(f"Testing test_cpe_get")
    status = await _get_http_status(
        api.cpe_get_with_http_info, "cpe:/a:microsoft:internet_explorer:8.0.6001:beta"
    )
    assert status == 200


async def _check_backup_get(api: EndpointsApi) -> None:
    print(f"Testing test_backup_get")
    status = await _get_http_status(api.backup_get_with_http_info)
    assert status == 200


async def _check_backup_index_get(api: EndpointsApi) -> None:
    print(f"Testing test_backup_index_get")
    status = await _get_http_status(api.backup_index_get_with_http_info, "initial-access")
    assert status == 200


async def _check_pdns_vulncheck_c2_get(api: EndpointsApi) -> None:
    print(f"Testing test_pdns_vulncheck_c2_get")
    status = await _get_http_status(api.pdns_vulncheck_c2_get_with_http_info, "")
    assert status == 200


async def _check_rules_initial_access_type_get(api: EndpointsApi) -> None:
    print(f"Testing test_rules_initial_access_type_get")
    status = await _get_http_status(
        api.rules_initial_access_type_get_with_http_info, "suricata"
    )
    assert status == 200


# --- IndicesApi Tests ---


async def _check_all_indices(indices: IndicesApi) -> None:
    targets = [
        "index_nist_nvd2_get_with_http_info",
        "index_vulncheck_kev_get_with_http_info",
        "index_ipintel3d_get_with_http_info",
        "index_cisa_kev_get_with_http_info",
    ]

    for name in targets:
        method = getattr(indices, name)
        status = await _get_http_status(method, 1, 1)
        print(f"Testing {name}: Result {status}")
        assert status == 200


# --- NvdApi Tests ---


async def _check_nvd(api: NvdApi) -> None:
    print("Testing NvdApi")
    cve_id = "CVE-2021-44228"

    cves = await api.nvd_cves_get(cve_id=cve_id)
    assert cves.total_results == 1
    assert cves.vulnerabilities[0].cve.id == cve_id

    first = await api.nvd_cves_get(cve_tag="disputed", results_per_page=5, cursor="")
    assert first.next_cursor
    second = await api.nvd_cves_get(cve_tag="disputed", results_per_page=5, cursor=first.next_cursor)
    assert second.vulnerabilities[0].cve.id != first.vulnerabilities[0].cve.id

    assert (await api.nvd_cve_history_get(cve_id=cve_id)).cve_changes
    assert (await api.nvd_cpes_get(cpe_match_string="cpe:2.3:a:apache:log4j", results_per_page=5)).products
    assert (await api.nvd_cpe_match_get(cve_id=cve_id, results_per_page=5)).match_strings
    assert (await api.nvd_source_get(results_per_page=5)).sources


# --- Orchestrator ---


async def main() -> None:
    if not API_TOKEN:
        print("Warning: VULNCHECK_API_TOKEN is not set.")

    config = vcaio.Configuration()
    config.api_key["Bearer"] = API_TOKEN

    # The 'async with' ensures the ClientSession is closed
    async with vcaio.ApiClient(config) as client:
        endpoints_api = vcaio.EndpointsApi(client)
        indices_api = vcaio.IndicesApi(client)

        print("--- Running Tests ---")
        await asyncio.gather(
            _check_openapi_get(endpoints_api),
            _check_entitlements_get(endpoints_api),
            _check_purl_get(endpoints_api),
            _check_index_get(endpoints_api),
            _check_cpe_get(endpoints_api),
            _check_backup_get(endpoints_api),
            _check_backup_index_get(endpoints_api),
            _check_pdns_vulncheck_c2_get(endpoints_api),
            _check_rules_initial_access_type_get(endpoints_api),
        )

        await _check_all_indices(indices_api)
        await _check_nvd(vcaio.NvdApi(client))

    # --- CRITICAL FIX FOR "UNCLOSED CONNECTOR" ---
    # aiohttp requires a small window of time to allow the
    # underlying SSL/TCP transports to finish closing.
    await asyncio.sleep(0.250)
    print("--- All Tests Completed Successfully ---")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
