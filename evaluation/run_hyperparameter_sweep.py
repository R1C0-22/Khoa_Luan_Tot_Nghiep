"""
Small hyperparameter sweep runner for AnRe.

Sweeps variables requested in IMPROVE.MD:
  - HISTORY_LENGTH_L (L)
  - SHORT_TERM_L (l)
  - DTF_ALPHA (alpha)

Usage:
  python -m evaluation.run_hyperparameter_sweep
"""

from __future__ import annotations

import os
from itertools import product

from colab_setup import test_prediction_metrics
from evaluation.experiment_io import (
    base_meta,
    make_run_dir,
    should_save_experiment,
    write_csv,
    write_json,
)
from evaluation.runtime import ensure_eval_runtime, patched_env


def _parse_list_env(name: str, default_csv: str) -> list[str]:
    raw = os.environ.get(name, default_csv)
    items = [x.strip() for x in raw.split(",")]
    return [x for x in items if x]


def main() -> None:
    ensure_eval_runtime()

    n_queries = int(os.environ.get("SWEEP_N_QUERIES", "10"))
    sample_size = int(os.environ.get("SWEEP_CLUSTER_SAMPLE", "500"))

    l_values = _parse_list_env("SWEEP_SHORT_TERM_L", "10,20,30")
    L_values = _parse_list_env("SWEEP_HISTORY_LENGTH_L", "50,100,150")
    a_values = _parse_list_env("SWEEP_DTF_ALPHA", "2.25,2.75,3.00")

    print("L,l,alpha,eval_filter,hit@1,hit@10,hit@1_filtered,hit@10_filtered,evaluated,skipped")
    rows: list[dict[str, str | float | int]] = []
    for L, l, alpha in product(L_values, l_values, a_values):
        patch = {
            "HISTORY_LENGTH_L": L,
            "SHORT_TERM_L": l,
            "DTF_ALPHA": alpha,
        }
        with patched_env(patch):
            result = test_prediction_metrics(
                n_queries=n_queries,
                sample_size=sample_size,
                use_second_order=False,
                start_index=0,
            )
        row = {
            "L": L,
            "l": l,
            "alpha": alpha,
            "eval_filter": str(result["eval_filter"]),
            "hit@1": float(result["hit_at_1"]),
            "hit@10": float(result["hit_at_10"]),
            "hit@1_filtered": float(result["hit_at_1_filtered"]),
            "hit@10_filtered": float(result["hit_at_10_filtered"]),
            "evaluated": int(result["evaluated"]),
            "skipped": int(result["skipped_gt_not_in_oq"]),
        }
        rows.append(row)
        print(
            f"{row['L']},{row['l']},{row['alpha']},{row['eval_filter']},"
            f"{row['hit@1']:.4f},{row['hit@10']:.4f},"
            f"{row['hit@1_filtered']:.4f},{row['hit@10_filtered']:.4f},"
            f"{row['evaluated']},{row['skipped']}"
        )

    if should_save_experiment():
        run_dir = make_run_dir("hyperparameter_sweep")
        meta = base_meta("evaluation.run_hyperparameter_sweep")
        meta.update(
            {
                "n_queries": n_queries,
                "sample_size": sample_size,
                "grid": {
                    "L_values": L_values,
                    "l_values": l_values,
                    "alpha_values": a_values,
                },
            }
        )
        write_json(
            run_dir / "meta.json",
            meta,
        )
        write_csv(run_dir / "metrics.csv", rows)
        print(f"\nSaved artifacts to: {run_dir}")


if __name__ == "__main__":
    main()

