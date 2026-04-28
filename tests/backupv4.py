import urllib.request
import vulncheck_sdk
from vulncheck_sdk.models.backup_list_backups_response import BackupListBackupsResponse
from vulncheck_sdk.models.backup_feed_item import BackupFeedItem
import os

TOKEN = os.environ["VULNCHECK_API_TOKEN"]

configuration = vulncheck_sdk.Configuration()
configuration.api_key["Bearer"] = TOKEN

with vulncheck_sdk.ApiClient(configuration) as api_client:
    backup_client = vulncheck_sdk.BackupApi(api_client)

    # List available backups (/v4/backup)
    available: BackupListBackupsResponse = backup_client.v4_list_backups()

    for potential_backup in available.data:
        print(f"Found backup: {potential_backup.name}")

    # Get backup for the wolfi feed (/v4/backup/wolfi)
    feed = "wolfi"
    response: BackupListBackupsResponse = backup_client.v4_get_backup_by_name(feed)

    print(response.to_json())

    print(f"Downloading {feed} backup")
    file_path = f"{feed}.zip"
    with urllib.request.urlopen(response.url_mrap) as r:
        with open(file_path, "wb") as f:
            f.write(r.read())

    print(f"Successfully saved to {file_path}")
