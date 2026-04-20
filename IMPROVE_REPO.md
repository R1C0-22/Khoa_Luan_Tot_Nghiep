# DOI CHIEU REPO THAM KHAO (BAN TOI GIAN)

Tai lieu nay chi ghi NHUNG GI DA AP DUNG that su trong codebase.

## Thu tu uu tien

1) `Document/De-Tai-2.pdf` (AnRe ACL 2025): cot loi phuong phap.  
2) `Code/IMPROVE.MD`: cac cai tien phuc vu khoa luan.  
3) Repo tham khao chi de engineering hygiene (KHONG thay doi cot loi AnRe):
- [usc-isi-i2/isi-tkg-icl](https://github.com/usc-isi-i2/isi-tkg-icl)
- [zjs123/TKG-Benchmark](https://github.com/zjs123/TKG-Benchmark)
- [waltbai/G2S-TKG-forecasting](https://github.com/waltbai/G2S-TKG-forecasting)
- [ZifengDing/zrLLM](https://github.com/ZifengDing/zrLLM)

## Da ap dung

- Giu nguyen pipeline AnRe: clustering -> dual history (PDC/DTF) -> analogical replay -> prediction.
- Giu va mo rong improve package: adaptive `Oq/O2q`, cache, parse index-first, sweep/ablation.
- Chuan hoa danh gia Hit@:
  - `EVAL_FILTER=none|static|time-aware`
  - posthoc eval tu JSONL.
- Chuan hoa artifact benchmark:
  - `results/<experiment>/<run_id>/meta.json` + `metrics.csv`
  - ap dung cho `run_ablation`, `run_hyperparameter_sweep`, `run_posthoc_eval`.
- Chuan hoa model/tokenizer setup:
  - `HF_TOKENIZER_ID`, `HF_USE_FAST_TOKENIZER` de test tokenizer compatibility.

## Co y khong dua vao

- 2-stage training cua G2S.
- supervised wrappers/fine-tune flow tu zrLLM.
- data format pickle/time-interval cua TKG-Benchmark.
- bat ky thay doi nao lam lech bai toan training-free AnRe.

## Ket luan

Codebase hien tai bam sat AnRe + `IMPROVE.MD`; repo ngoai chi dung de tang tinh reproducibility, benchmark hygiene, va do on dinh khi trien khai.
