import vulncheck_sdk
import os

TOKEN = os.environ["VULNCHECK_API_TOKEN"]

configuration = vulncheck_sdk.Configuration()
configuration.api_key["Bearer"] = TOKEN

with vulncheck_sdk.ApiClient(configuration) as api_client:
    nvd_client = vulncheck_sdk.NvdApi(api_client)

    # Look up a single CVE, shaped exactly as NVD's API returns it
    api_response = nvd_client.nvd_cves_get(cve_id="CVE-2021-44228")
    cve = api_response.vulnerabilities[0].cve
    print(cve.id, cve.vuln_status)

    # Walk every CVE modified in a date range. Sending an empty cursor opts in
    # to cursor paging; each response then carries the cursor for the next page
    cursor = ""
    while cursor is not None:
        api_response = nvd_client.nvd_cves_get(
            last_mod_start_date="2026-09-01T00:00:00.000",
            last_mod_end_date="2026-09-02T00:00:00.000",
            results_per_page=500,
            cursor=cursor,
        )
        print(len(api_response.vulnerabilities), "of", api_response.total_results)
        cursor = api_response.next_cursor
