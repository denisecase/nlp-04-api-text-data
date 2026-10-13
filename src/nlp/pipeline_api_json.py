"""pipeline_api_json.py - Module 4 Script.

(NO EDITS REQUIRED IN THIS FILE)

Purpose

  Orchestrate a standard ETL/EVTL pipeline.
  Illustrate how to extract JSON data from an API, validate it, transform it, and load it into a sink.
  Illustrate how to parse JSON to get the desired information.


Analytical Questions

- How can we extract JSON data from an API and save it to a file?
- How can we validate the structure and content of the JSON data?
- How can we transform the validated JSON data into a structured format (like a DataFrame)?
- How can we load the transformed data into a sink (like a CSV file)?


Notes:
- This file should not require modification.
- This is the main pipeline script that orchestrates the entire EVTL process.
- It assumes a standard ETL pipeline enhanced with a VALIDATE stage, making it an EVTL pipeline.
- The stages are modularized into separate files for clarity and maintainability.
- Each stage has its own source and sink, which are clearly indicated in the stage files.
- The configuration values (like API URL and file paths) are stored in a separate config file.

Run from root project folder with:

  uv run python -m nlp.pipeline_api_json
"""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging

from datafun_toolkit.logger import get_logger, log_header, log_path

from nlp.config import (
    API_URL,
    DATA_PATH,
    HTTP_REQUEST_HEADERS,
    PROCESSED_CSV_PATH,
    PROCESSED_PATH,
    RAW_JSON_PATH,
    RAW_PATH,
    ROOT_PATH,
)
from nlp.stage01_extract import run_extract
from nlp.stage02_validate import run_validate
from nlp.stage03_transform import run_transform
from nlp.stage04_load import run_load

# ============================================================
# Section 2. Configure Logging
# ============================================================

LOG: logging.Logger = get_logger("CI", level="DEBUG")


# ============================================================
# Section 3. Define Main Pipeline Function
# ============================================================


def main() -> None:
    """Main function - this is where the execution begins."""
    log_header(LOG, "MODULE 4: EVTL PIPELINE")
    LOG.info("START PIPELINE")

    RAW_PATH.mkdir(parents=True, exist_ok=True)
    PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

    log_path(LOG, "ROOT_PATH", ROOT_PATH)
    log_path(LOG, "DATA_PATH", DATA_PATH)
    log_path(LOG, "RAW_PATH", RAW_PATH)
    log_path(LOG, "PROCESSED_PATH", PROCESSED_PATH)

    # EXTRACT
    json_data = run_extract(
        source_api_url=API_URL,
        http_request_headers=HTTP_REQUEST_HEADERS,
        raw_json_path=RAW_JSON_PATH,
        LOG=LOG,
    )

    # VALIDATE
    validated_data = run_validate(
        json_data=json_data,
        LOG=LOG,
    )

    # TRANSFORM
    df = run_transform(
        json_data=validated_data,
        LOG=LOG,
    )

    # LOAD
    run_load(
        df=df,
        processed_csv_path=PROCESSED_CSV_PATH,
        LOG=LOG,
    )

    LOG.info("========================")
    LOG.info("Pipeline executed successfully!")
    LOG.info("========================")


# ============================================================
# Section 4. Run Main Function when This File is Executed
# ============================================================

if __name__ == "__main__":
    main()
