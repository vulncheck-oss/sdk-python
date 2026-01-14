import pytest
import subprocess
import os
import sys
import vulncheck_sdk
from vulncheck_sdk.api.endpoints_api import EndpointsApi
from vulncheck_sdk.api.indices_api import IndicesApi
from vulncheck_sdk.api_response import ApiResponse
from vulncheck_sdk.exceptions import ApiException, UnauthorizedException

DEFAULT_HOST = "https://api.vulncheck.com"
DEFAULT_API = DEFAULT_HOST + "/v3"
API_TOKEN = os.environ["VULNCHECK_API_TOKEN"]


# List of python programs to test
PROGRAMS = ["./tests/backup.py", "./tests/cpe.py", "./tests/index.py", "./tests/indicies.py","./tests/pagination.py","./tests/purl.py","./tests/quickstart.py","./tests/purl_aio.py"]

@pytest.mark.parametrize("program_file", PROGRAMS)
def test_external_program(program_file):
    """
    Runs an external python program with a specific TOKEN env var.
    Fails if the program returns a non-zero exit code.
    """
    
    # verify file exists before trying to run it
    if not os.path.exists(program_file):
        pytest.fail(f"Program file not found: {program_file}")

    # Execute the program
    # capture_output=True allows us to see stdout/stderr if the test fails
    result = subprocess.run(
        [sys.executable, program_file],
        env=os.environ.copy(),
        capture_output=True,
        text=True
    )

    # Assert Success
    # If this fails, pytest will print the error message including stdout/stderr
    assert result.returncode == 0, (
        f"Script failed with exit code {result.returncode}.\n"
        f"--- STDOUT ---\n{result.stdout}\n"
        f"--- STDERR ---\n{result.stderr}\n"
    )