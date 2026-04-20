# DOI CHIEU REPO THAM KHAO (BAN TINH GON)

Tai lieu nay tom tat nhung gi da AP DUNG that su trong codebase, theo thu tu uu tien:
1) `Document/De-Tai-2.pdf` (AnRe ACL 2025): cot loi phuong phap.
2) `Code/IMPROVE.MD`: goi cai tien phuc vu khoa luan.
3) Repos tham khao (isi-tkg-icl / TKG-Benchmark / G2S / zrLLM): chi dung cho engineering hygiene.

## 1) Nhung gi GIU NGUYEN theo paper + improve

- Kien truc AnRe: semantic clustering -> dual history (short + long PDC/DTF) -> analogical replay -> predict.
- Hyperparameter theo paper: sweep `L`, `l`, `alpha`; default paper-like `L=100`, `l=20`, `alpha=2.75`.
- Cai tien IMPROVE: adaptive `Oq/O2q`, cache LLM, parse index uu tien, benchmark cache, ablation mini.

## 2) Nhung gi da lay tu repo tham khao

- Chuan hoa danh gia Hit@:
  - Filter mode `none/static/time-aware`.
  - Posthoc eval tu JSONL.
- Chuan hoa artifact benchmark:
  - Luu `results/<experiment>/<run_id>/meta.json` + `metrics.csv`.
  - Ap dung cho `run_ablation`, `run_hyperparameter_sweep`, `run_posthoc_eval`.
- Chuan hoa cau hinh model/tokenizer:
  - Ho tro tokenizer override (`HF_TOKENIZER_ID`, `HF_USE_FAST_TOKENIZER`) de test tokenizer compatibility khi doi model HF.

## 3) Nhung gi KHONG dua vao code (co y)

- Khong dua 2-stage training cua G2S.
- Khong dua supervised wrappers tu zrLLM.
- Khong doi pipeline sang data format pickle/time-interval cua TKG-Benchmark.
- Khong doi bai toan training-free AnRe sang huong fine-tune.

## 4) Ket luan

- Codebase hien tai bam sat AnRe + IMPROVE.MD.
- Repo ngoai chi duoc dung de nang do on dinh/chuan hoa thuc nghiem, khong thay doi cot loi hoc thuat.
