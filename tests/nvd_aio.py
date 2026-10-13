import asyncio
import os
import vulncheck_sdk.aio as vcaio

TOKEN = os.environ.get("VULNCHECK_API_TOKEN")

configuration = vcaio.Configuration()
configuration.api_key["Bearer"] = TOKEN


async def main():
    async with vcaio.ApiClient(configuration) as api_client:
        nvd_client = vcaio.NvdApi(api_client)

        # Look up a single CVE, shaped exactly as NVD's API returns it
        api_response = await nvd_client.nvd_cves_get(cve_id="CVE-2021-44228")
        cve = api_response.vulnerabilities[0].cve
        print(cve.id, cve.vuln_status)

        # Walk every CVE modified in a date range. Sending an empty cursor opts
        # in to cursor paging; each response then carries the cursor for the
        # next page
        cursor = ""
        while cursor is not None:
            api_response = await nvd_client.nvd_cves_get(
                last_mod_start_date="2026-09-01T00:00:00.000",
                last_mod_end_date="2026-09-02T00:00:00.000",
                results_per_page=500,
                cursor=cursor,
            )
            print(len(api_response.vulnerabilities), "of", api_response.total_results)
            cursor = api_response.next_cursor


if __name__ == "__main__":
    asyncio.run(main())
