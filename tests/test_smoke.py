"""Offline smoke tests for the JSON API EVTL stages."""

import json
import logging
from types import SimpleNamespace

import polars as pl
import pytest
import requests

from nlp.stage01_extract import run_extract
from nlp.stage02_validate import run_validate
from nlp.stage03_transform import run_transform
from nlp.stage04_load import run_load


def test_json_stages_write_expected_csv(monkeypatch, tmp_path):
    """Run extraction through loading with a controlled API response."""
    rows = [
        {"userId": 7, "id": 11, "title": "Text mining", "body": "Short example"},
        {"userId": 8, "id": 12, "title": "NLP", "body": "Another document"},
    ]
    payload = json.dumps(rows)

    def fake_get(url, *, headers, timeout):
        assert url == "https://example.test/posts"
        assert headers["Accept"] == "application/json"
        assert timeout == 30
        return SimpleNamespace(
            text=payload,
            json=lambda: json.loads(payload),
            raise_for_status=lambda: None,
        )

    monkeypatch.setattr(requests, "get", fake_get)
    log = logging.getLogger(__name__)
    raw_path = tmp_path / "raw.json"
    csv_path = tmp_path / "processed.csv"

    extracted = run_extract(
        "https://example.test/posts", {"Accept": "application/json"}, raw_path, log
    )
    df = run_transform(run_validate(extracted, log), log)
    run_load(df, csv_path, log)

    assert json.loads(raw_path.read_text(encoding="utf-8")) == rows
    assert csv_path.stat().st_size > 0
    saved = pl.read_csv(csv_path)
    assert saved["post_id"].to_list() == [11, 12]
    assert saved["title_length"].to_list() == [11, 3]
    assert saved["body_length"].to_list() == [13, 16]


def test_validation_rejects_empty_records():
    """Reject an empty API response instead of creating an empty dataset."""
    with pytest.raises(ValueError, match="at least one record"):
        run_validate([], logging.getLogger(__name__))
