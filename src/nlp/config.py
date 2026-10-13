"""config.py.

(EDIT YOUR VERSION OF THIS FILE)

Purpose

  Store configuration values for the EVTL pipeline.

Analytical Questions

- What API endpoint should be used as the data source?
- What HTTP request headers are required?
- Where should raw and processed data be stored?

Notes:
Following our process, do NOT edit this  file directly,
keep it as a working example.

In your custom project,copy this .py file and
append with _yourname.py instead.

Then edit your copied Python file to change:
- API URL (source of the JSON data),
- the HTTP Request Headers (to show your app name in the user-agent header)
- customize your output file name.
"""

from pathlib import Path

# ============================================================
# API CONFIGURATION
# ============================================================

# TODO: In your custom app, change the URL to work with a different API that returns JSON data.
API_URL: str = "https://jsonplaceholder.typicode.com/posts"

# TODO: In your custom app, change the header user-agent value
# to something that represents your app or project.
HTTP_REQUEST_HEADERS: dict[str, str] = {
    "User-Agent": "nlp-module-4-case/1.0",
    "Accept": "application/json",
}

# ============================================================
# PATH CONFIGURATION
# ============================================================

ROOT_PATH: Path = Path.cwd()
DATA_PATH: Path = ROOT_PATH / "data"
RAW_PATH: Path = DATA_PATH / "raw"
PROCESSED_PATH: Path = DATA_PATH / "processed"

# TODO: In your custom app, change the output file names from case_
# to something that represents YOUR custom project.
RAW_JSON_PATH: Path = RAW_PATH / "case_raw.json"
PROCESSED_CSV_PATH: Path = PROCESSED_PATH / "case_processed.csv"
