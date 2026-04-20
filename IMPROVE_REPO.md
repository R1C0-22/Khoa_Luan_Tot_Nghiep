# DOI CHIEU REPO THAM KHAO (BAN TINH GON)

## Thu tu uu tien
1) `Document/De-Tai-2.pdf` (AnRe ACL 2025) - cot loi phuong phap.  
2) `Code/IMPROVE.MD` - cai tien khoa luan.  
3) Repo tham khao chi de engineering hygiene (khong doi core AnRe):
- [usc-isi-i2/isi-tkg-icl](https://github.com/usc-isi-i2/isi-tkg-icl)
- [zjs123/TKG-Benchmark](https://github.com/zjs123/TKG-Benchmark)
- [waltbai/G2S-TKG-forecasting](https://github.com/waltbai/G2S-TKG-forecasting)
- [ZifengDing/zrLLM](https://github.com/ZifengDing/zrLLM)

## Da ap dung vao code
- Giu nguyen AnRe pipeline: clustering -> dual history (PDC/DTF) -> analogical replay -> prediction.
- Giu improve package: adaptive `Oq/O2q`, cache, parse index-first, sweep + ablation.
- Chuan hoa Hit@ eval: `EVAL_FILTER=none|static|time-aware` + posthoc eval tu JSONL.
- Chuan hoa artifact benchmark: `results/<experiment>/<run_id>/meta.json` + `metrics.csv`.
- Chuan hoa tokenizer benchmark cho HF: `HF_TOKENIZER_ID`, `HF_USE_FAST_TOKENIZER`.

## Khong ap dung (de tranh lech de tai)
- 2-stage training cua G2S.
- supervised wrappers/fine-tune flow cua zrLLM.
- data format pickle/time-interval cua TKG-Benchmark.
- bat ky thay doi nao lam lech bai toan training-free AnRe.

## Ket luan
Codebase giu core AnRe + `IMPROVE.MD`; repo ngoai chi duoc dung de tang reproducibility, benchmark hygiene, va do on dinh khi trien khai.
