"""
Small helpers to store reproducible evaluation artifacts.

Inspired by benchmark-style experiment organization:
  results/<experiment>/<run_id>/{meta.json,metrics.csv}
"""

from __future__ import annotations

import csv
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any


def make_run_dir(experiment_name: str) -> Path:
    """Create and return a timestamped run directory."""
    root = os.environ.get("EXPERIMENT_ROOT", "results").strip() or "results"
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    out = Path(root) / experiment_name / run_id
    out.mkdir(parents=True, exist_ok=True)
    return out


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as fw:
        writer = csv.DictWriter(fw, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

