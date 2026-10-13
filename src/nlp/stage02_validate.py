"""stage02_validate.py.

(EDIT YOUR VERSION OF THIS FILE)

Source: raw JSON object
Sink: validated JSON object

Purpose

  Inspect JSON structure and validate that the data is usable.

Analytical Questions

- What is the top-level structure of the JSON data?
- What keys are present in each record?
- What data types are associated with each field?
- Does the data meet expectations for transformation?

Notes:
Following our process, do NOT edit this  file directly,
keep it as a working example.

In your custom project, copy this .py file and
append with _yourname.py instead.

Then edit your copied Python file to:
- inspect the JSON structure for your API,
- validate required keys and types,
- confirm the data is usable for your analysis.
"""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging
from typing import Any

# ============================================================
# Section 2. Define Run Validate Function
# ============================================================


def run_validate(
    json_data: Any,
    LOG: logging.Logger,
) -> list[dict]:
    """Inspect and validate JSON structure.

    Args:
        json_data (Any): The raw JSON data from the Extract stage.
        LOG (logging.Logger): The logger instance.

    Returns:
        list[dict]: The validated JSON data.
    """
    LOG.info("========================")
    LOG.info("STAGE 02: VALIDATE starting...")
    LOG.info("========================")

    # ============================================================
    # INSPECT JSON STRUCTURE
    # ============================================================

    LOG.info("JSON STRUCTURE INSPECTION:")

    # Log the type of the top-level JSON structure.
    # Use the built-in type() function to get the type
    # and built-in variable __name__ to log just the type name.
    LOG.info(f"Top-level type: {type(json_data).__name__}")

    if isinstance(json_data, list) and len(json_data) > 0:
        first_record = json_data[0]

        LOG.info(f"Keys in first record: {list(first_record.keys())}")

        LOG.info("Field types:")
        for key, value in first_record.items():
            LOG.info(f"{key}: {type(value).__name__}")

    # ============================================================
    # VALIDATE EXPECTATIONS
    # ============================================================

    if not isinstance(json_data, list):
        raise TypeError("Expected JSON data to be a list of records.")

    if len(json_data) == 0:
        raise ValueError("Expected at least one record.")

    if not all(isinstance(record, dict) for record in json_data):
        raise ValueError("Expected each record to be a dictionary.")

    LOG.info("Validation passed.")
    LOG.info("Sink: validated JSON object")

    # Return the validated JSON data for use in the next stage.
    return json_data
