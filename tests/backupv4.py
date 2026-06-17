import os
import tempfile
import urllib.request

from urllib3.util.retry import Retry

import vulncheck_sdk
from vulncheck_sdk.models.backup_backup_response import BackupBackupResponse
from vulncheck_sdk.models.backup_list_backups_response import BackupListBackupsResponse

TOKEN = os.environ["VULNCHECK_API_TOKEN"]

configuration = vulncheck_sdk.Configuration()
configuration.api_key["Bearer"] = TOKEN
configuration.retries = Retry(
    total=5,
    backoff_factor=2,
    status_forcelist=[502, 503, 504],
    allowed_methods=["GET"],
    respect_retry_after_header=True,
)

with vulncheck_sdk.ApiClient(configuration) as api_client:
    backup_client = vulncheck_sdk.BackupApi(api_client)

    # List available backups (/v4/backup)
    available: BackupListBackupsResponse = backup_client.v4_list_backups()

    for potential_backup in available.data:
        print(f"Found backup: {potential_backup.name}")

    # Get backup for the wolfi feed (/v4/backup/wolfi)
    feed = "wolfi"
    response: BackupBackupResponse = backup_client.v4_get_backup_by_name(feed)

    print(response.to_json())

    print(f"Downloading {feed} backup")
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, f"{feed}.zip")
        with urllib.request.urlopen(response.url_mrap) as r:
            with open(file_path, "wb") as f:
                f.write(r.read())
        print(f"Successfully saved to {file_path}")
