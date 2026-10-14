"""stage01_extract.py - Stage 01: Extract.

NO EDITS REQUIRED IN THIS FILE (if paths have not changed.)

Source: API
Sink: raw JSON object + raw JSON file

The Extract stage is responsible for retrieving data
from the source (in this case, an API)
and saving it to a file.
It also returns the extracted data as a Python object
for use in subsequent stages.

Notes:
- This file should not require modification.
"""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging
from pathlib import Path
from typing import Any

from datafun_toolkit.logger import log_path
import requests

# ============================================================
# Section 2. Define Run Extract Function
# ============================================================


def run_extract(
    source_api_url: str,
    http_request_headers: dict[str, str],
    raw_json_path: Path,
    LOG: logging.Logger,
) -> Any:
    """Extract JSON data from the API and save it to a file.

    Args:
        source_api_url (str): The URL of the API endpoint.
        http_request_headers (dict[str, str]): The HTTP request headers.
        raw_json_path (Path): The path to save the raw JSON file.
        LOG (logging.Logger): The logger instance.

    Returns:
        Any: The extracted JSON data as a Python object (e.g., a list or dictionary).

    Raises:
        requests.HTTPError: If the HTTP request to the API fails.
        requests.RequestException: For other types of request exceptions.
        ValueError: If the response content cannot be parsed as JSON.
    """
    LOG.info("========================")
    LOG.info("STAGE 01: EXTRACT starting... ")
    LOG.info("========================")

    # Use the requests.get() function to make an HTTP GET request
    # to the source_api_url with the provided headers.
    response = requests.get(source_api_url, headers=http_request_headers, timeout=30)

    # Use the raise_for_status() method to check for HTTP errors
    # and raise an exception if the request was unsuccessful.
    response.raise_for_status()

    # Use the .json() method of the response object to parse the JSON content
    # and store it in a variable called json_data.
    json_data: Any = response.json()

    # Use the write_text() method of the raw_json_path to
    # save the raw JSON data to a file.
    # Specify the encoding as "utf-8" to ensure proper handling of special characters.
    raw_json_path.write_text(response.text, encoding="utf-8")

    # Use log.info() to log the source API URL (a string).
    # Use a formatted string (f-string) to include the variable in the log message.
    LOG.info(f"SOURCE PATH = {source_api_url}")

    # Use the privacy-conscious
    # log_path function to log the sink path.
    log_path(LOG, "SINK PATH", raw_json_path)

    # Return the extracted JSON data as a Python object (e.g., a list or dictionary).
    return json_data
