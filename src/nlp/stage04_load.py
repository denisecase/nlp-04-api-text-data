"""stage04_load.py.

(NO EDITS REQUIRED IN THIS FILE)

Source: DataFrame
Sink: CSV file

Notes:
- This file should not require modification.
"""

# ============================================================
# Section 1. Setup and Imports
# ============================================================

import logging
from pathlib import Path

from datafun_toolkit.logger import log_path
import polars as pl

# ============================================================
# Section 2. Define Run Load Function
# ============================================================


def run_load(
    df: pl.DataFrame,
    processed_csv_path: Path,
    LOG: logging.Logger,
) -> None:
    """Write DataFrame to CSV sink.

    Args:
        df (pl.DataFrame): The DataFrame to write.
        processed_csv_path (Path): The path to save the processed CSV file.
        LOG (logging.Logger): The logger instance.

    Returns:
        None (just writes to the sink)
    """
    LOG.info("========================")
    LOG.info("STAGE 04: LOAD starting...")
    LOG.info("========================")

    df.write_csv(processed_csv_path)

    # Use the privacy-conscious
    # log_path function to log the sink path.
    log_path(LOG, "SINK PATH", processed_csv_path)
