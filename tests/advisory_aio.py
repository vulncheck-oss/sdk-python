import asyncio
import os
import vulncheck_sdk.aio as vcaio
from vulncheck_sdk.aio.models.search_v4_advisory_return_value import SearchV4AdvisoryReturnValue
from vulncheck_sdk.aio.models.search_v4_list_feed_return_value import SearchV4ListFeedReturnValue

TOKEN = os.environ.get("VULNCHECK_API_TOKEN")

configuration = vcaio.Configuration()
configuration.api_key["Bearer"] = TOKEN


async def main():
    async with vcaio.ApiClient(configuration) as api_client:
        advisory_client = vcaio.AdvisoryApi(api_client)

        # List all available advisory feeds (/v4/advisory)
        feeds: SearchV4ListFeedReturnValue = await advisory_client.v4_list_advisory_feeds()
        print("Available feeds:")
        for feed in feeds.data:
            print(f"name: {feed.name}")

        feed = "wolfi"
        # Query advisories filtered by feed=wolfi (/v4/advisory?feed=wolfi)
        advisories: SearchV4AdvisoryReturnValue = await advisory_client.v4_query_advisories(name=feed)
        print(f"{feed.capitalize()} advisories (page 1): {len(advisories.data)} results")
        for advisory in advisories.data:
            print(f"cve: {advisory.cve_metadata.cve_id}")


if __name__ == "__main__":
    asyncio.run(main())
