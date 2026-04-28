import asyncio
import os
import urllib.request
import vulncheck_sdk.aio as vcaio
from vulncheck_sdk.aio.models.backup_list_backups_response import BackupListBackupsResponse
from vulncheck_sdk.aio.models.backup_backup_response import BackupBackupResponse

TOKEN = os.environ.get("VULNCHECK_API_TOKEN")

configuration = vcaio.Configuration()
configuration.api_key["Bearer"] = TOKEN


def download_sync(url, file_path):
    """
    Standard synchronous download using urllib.request.
    This runs in a separate thread to avoid blocking the event loop.
    """
    with urllib.request.urlopen(url) as response:
        with open(file_path, "wb") as file:
            file.write(response.read())


async def main():
    async with vcaio.ApiClient(configuration) as api_client:
        backup_client = vcaio.BackupApi(api_client)

        # List available backups (/v4/backup)
        available: BackupListBackupsResponse = await backup_client.v4_list_backups()
        for potential_backup in available.data:
            print(f"Found backup: {potential_backup.name}")

        # Get backup for the wolfi feed (/v4/backup/wolfi)
        feed = "wolfi"
        response: BackupBackupResponse = await backup_client.v4_get_backup_by_name(feed)

        print(response.to_json())

        file_path = f"{feed}.zip"
        print(f"Downloading {feed} backup via urllib (offloaded to thread)...")

        await asyncio.to_thread(download_sync, response.url, file_path)

        print(f"Successfully saved to {file_path}")


if __name__ == "__main__":
    asyncio.run(main())
