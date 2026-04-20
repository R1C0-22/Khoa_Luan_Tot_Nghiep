"""
Unified CLI runner for evaluation tasks.

Examples
--------
python -m evaluation.run_experiments --task ablation --n-queries 20 --sample-size 800
python -m evaluation.run_experiments --task sweep --n-queries 10 --sample-size 500
python -m evaluation.run_experiments --task posthoc --records-path outputs/predictions.jsonl --eval-filter time-aware
"""

from __future__ import annotations

import argparse
import os
from contextlib import contextmanager
from typing import Iterator


@contextmanager
def _patched_env(patch: dict[str, str]) -> Iterator[None]:
    old = {k: os.environ.get(k) for k in patch}
    try:
        for k, v in patch.items():
            os.environ[k] = v
        yield
    finally:
        for k, v in old.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v


def _get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run standardized evaluation tasks.")
    parser.add_argument(
        "--task",
        required=True,
        choices=["ablation", "sweep", "posthoc"],
        help="Which evaluation task to run.",
    )
    parser.add_argument("--n-queries", type=int, default=None, help="Override query count for ablation/sweep.")
    parser.add_argument("--sample-size", type=int, default=None, help="Override cluster sample size for ablation/sweep.")
    parser.add_argument(
        "--eval-filter",
        type=str,
        default=None,
        choices=["none", "static", "time-aware"],
        help="Optional eval filter override.",
    )
    parser.add_argument("--records-path", type=str, default=None, help="Path to predictions jsonl (for posthoc).")
    parser.add_argument("--save-experiment", type=int, default=None, choices=[0, 1], help="Set SAVE_EXPERIMENT=0/1.")
    return parser.parse_args()


def main() -> None:
    args = _get_args()

    patch: dict[str, str] = {}
    if args.eval_filter is not None:
        patch["EVAL_FILTER"] = args.eval_filter
    if args.save_experiment is not None:
        patch["SAVE_EXPERIMENT"] = str(args.save_experiment)

    if args.task == "ablation":
        from evaluation.run_ablation import main as run_ablation_main

        if args.n_queries is not None:
            patch["ABLATION_N_QUERIES"] = str(args.n_queries)
        if args.sample_size is not None:
            patch["ABLATION_CLUSTER_SAMPLE"] = str(args.sample_size)
        with _patched_env(patch):
            run_ablation_main()
        return

    if args.task == "sweep":
        from evaluation.run_hyperparameter_sweep import main as run_sweep_main

        if args.n_queries is not None:
            patch["SWEEP_N_QUERIES"] = str(args.n_queries)
        if args.sample_size is not None:
            patch["SWEEP_CLUSTER_SAMPLE"] = str(args.sample_size)
        with _patched_env(patch):
            run_sweep_main()
        return

    from evaluation.run_posthoc_eval import main as run_posthoc_main
    if args.records_path:
        patch["EVAL_RECORDS_PATH"] = args.records_path
    with _patched_env(patch):
        run_posthoc_main()


if __name__ == "__main__":
    main()

