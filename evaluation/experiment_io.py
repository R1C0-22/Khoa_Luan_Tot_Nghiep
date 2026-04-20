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


def should_save_experiment() -> bool:
    """Return whether evaluation scripts should persist run artifacts."""
    raw = os.environ.get("SAVE_EXPERIMENT", "1").strip().lower()
    return raw in {"1", "true", "yes", "on"}


def base_meta(script_name: str) -> dict[str, Any]:
    """Common metadata shared by evaluation scripts."""
    return {
        "script": script_name,
        "llm_provider": os.environ.get("LLM_PROVIDER", ""),
        "hf_model_id": os.environ.get("HF_MODEL_ID", ""),
        "hf_tokenizer_id": os.environ.get("HF_TOKENIZER_ID", ""),
        "eval_filter": os.environ.get("EVAL_FILTER", "none"),
    }


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

