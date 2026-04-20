# DOI CHIEU 5 NGUON (THEO UU TIEN)

Tai lieu nay duoc doi chieu theo dung thu tu uu tien:
1) `Document/De-Tai-2.pdf` (paper AnRe, ACL 2025) - NEN TANG COT LOI.
2) `Code/IMPROVE.MD` - GOI CAI TIEN PHUC VU KHOA LUAN.
3) `https://github.com/usc-isi-i2/isi-tkg-icl` - NGUON THAM KHAO DE FIX BUG/TOI UU MOT PHAN.
4) `https://github.com/zjs123/TKG-Benchmark` - NGUON THAM KHAO DE CHUAN HOA THUC NGHIEM/OUTPUT.
5) `https://github.com/waltbai/G2S-TKG-forecasting` + `https://github.com/ZifengDing/zrLLM` - NGUON THAM KHAO DE CHUAN HOA CONFIG/RUNNER/TEST HYGIENE.

Ket luan dinh vi:
- Code hien tai CHU YEU duoc xay tren (1) + (2).
- (3) duoc dung o vai diem ky thuat de on dinh he thong, KHONG phai nguon cot loi cua de tai.
- (4) duoc dung de chuan hoa artifact va quy trinh benchmark, KHONG thay doi logic cot loi AnRe.
- (5) duoc dung de chuan hoa cach to chuc config-script-test, KHONG lay co che training cua repo ngoai de thay logic training-free AnRe.

---

## 1) Cot loi tu (1) `De-Tai-2.pdf` da duoc ap dung

### A. Kien truc AnRe giu dung huong paper
- Semantic-driven historical clustering.
- Dual history extraction (short-term + long-term PDC/DTF).
- Analogical replay de tao reasoning examples.
- Final prediction theo candidate set va chon ket qua xep hang cao nhat.

### B. Hyperparameter va thiet ke thuc nghiem dung tinh than paper
- Co truc sweep cho `L`, `l`, `alpha` (phu hop phan 6.1 cua paper).
- Co ablation mini: w/o long-term, w/o short-term, w/o analogical.
- Co ghi nhan trade-off candidate set 1-hop/2-hop (phan tich giong muc 6.2 paper).

### C. Prompting theo 3 giai doan paper
- Prompt cho PDC (chon su kien huu ich nhat).
- Prompt cho analysis process (APC / analogical explanation).
- Prompt cho object prediction (OEP, tra ve chi so candidate).

=> Ve hoc thuat, code dang bam sat cot song cua AnRe (nguon 1).

## 2) Phan tu (2) `IMPROVE.MD` da duoc dua vao code

### A. Goi cai tien "de lam khoa luan"
- Adaptive `Oq/O2q` (mo rong candidate dong thay vi co dinh).
- LLM caching cho scorer/generator/predictor.
- Runtime benchmark de bao cao giam thoi gian do cache.
- Hyperparameter sweep + ablation de phuc vu bao cao/bao ve.

### B. Cac sua bug-trong-tam da phan anh trong code
- Parse prediction theo chi so `1..|Oq|` uu tien truoc substring.
- Gioi han duong logprob khi candidate qua lon (`MAX_LOGPROB_CANDIDATES`).
- HF logprob fix loi va cham token dau (`1` vs `10` vs `100`).

=> Day la lop cai tien de bai toan chay on dinh va co du so lieu bao cao.

## 3) Vai tro thuc te cua (3) `isi-tkg-icl`

### A. Da tham khao va ap dung mot phan de on dinh pipeline
- Filtered eval mode `none/static/time-aware`.
- Tu duy runner/eval theo output JSONL.
- Mot so ky thuat map-label + ranking khi infer voi LLM.

### B. Nhung gi CHUA (va KHONG bat buoc) phai dong bo theo repo tham chieu
- Baseline `recency/frequency` theo dung script goc.
- Bo runner CLI y het (`run_hf.py`, `run_openai.py`, `run_rule.py`).
- Full protocol head/tail nhu repo goc ICL 2023.

=> Nguon (3) la bo tham chieu huu ich de sua bug, khong doi vai tro cot loi cua de tai.

## 4) Vai tro thuc te cua (4) `zjs123/TKG-Benchmark`

### A. Da tham khao va ap dung mot phan de chuan hoa thuc nghiem
- Chuan hoa artifact thuc nghiem theo run directory: `results/<experiment>/<run_id>/meta.json` va `results/<experiment>/<run_id>/metrics.csv`.
- Ap dung cho cac script danh gia: `evaluation.run_ablation`, `evaluation.run_hyperparameter_sweep`, `evaluation.run_posthoc_eval`.
- Them metadata moi run de tai lap de dang: script name, so query, sample size, eval filter, provider/model.
- Cho phep bat/tat luu artifact bang env: `SAVE_EXPERIMENT=1|0` (mac dinh bat).

### B. Nhung gi CHUA (va KHONG bat buoc) phai dong bo theo repo benchmark
- Khung train supervised cua benchmark (khong phu hop bai toan training-free AnRe hien tai).
- Data format pickle/stamp-span task (khong thay the pipeline quadruple `(s, r, o, t)` dang dung).

=> Nguon (4) duoc dung de nang tinh reproducibility va benchmark hygiene, khong doi vai tro cot loi cua de tai.

---

## 5) Vai tro thuc te cua (5) `G2S-TKG-forecasting` + `zrLLM`

### A. Da tham khao va co the ap dung de chuan hoa codebase
- Chuan hoa profile cau hinh theo file/entrypoint (tu duy tu `config/` cua G2S), thay vi phu thuoc env roi rac trong notebook.
- Chuan hoa script "prepare -> run -> evaluate" va naming convention cho thuc nghiem de de tai lap.
- Bo sung smoke-test / module-test toi thieu cho cac module critical (`inference`, `long_term`, `evaluation`) theo tinh than test folder cua G2S.
- Chuan hoa artifact run theo metadata day du (model alias, provider, preset, n_queries, sample_size, filter) de so sanh cong bang.

### B. Nhung gi KHONG nen lay truc tiep tu 2 repo nay
- Co che huan luyen 2-stage (General-to-Specific) cua G2S vi khong phu hop muc tieu training-free AnRe.
- He thong "LLM-enhanced supervised baselines" cua zrLLM (gamma/init/fine-tune wrappers) vi se lam lech cot loi bai toan hien tai.
- Hyperparameter/CLI cua repo ngoai neu khong map truc tiep voi ky hieu va thuc nghiem trong `De-Tai-2.pdf`.

=> Nguon (5) phu hop nhat de nang "engineering hygiene" (config, runner, test, reproducibility), khong de thay doi phuong phap cot loi.

---

## 6) Ket luan doi chieu theo uu tien 1 -> 2 -> 3 -> 4 -> 5

### Tuyen bo hoc thuat (de dua vao mo ta khoa luan)
- Nen tang phuong phap cua code la AnRe (nguon 1).
- Huong cai tien va muc tieu bao cao den tu `IMPROVE.MD` (nguon 2).
- `isi-tkg-icl` (nguon 3) chi dong vai tro tham khao ky thuat de giam bug va tang do on dinh khi trien khai.
- `TKG-Benchmark` (nguon 4) chi dong vai tro tham khao chuan hoa quy trinh va artifact thuc nghiem.
- `G2S` + `zrLLM` (nguon 5) chi dong vai tro tham khao chuan hoa config/script/test, khong doi sang bai toan training.

### Cac diem nen nhan manh khi bao ve
- Khung bai toan va module theo paper AnRe duoc giu nguyen tinh than.
- Co bo cai tien thuc dung, giai quyet han che runtime/oom/parse sai.
- Co thuc nghiem bo tro (ablation, sweep, cache benchmark) de chung minh gia tri ky thuat.

## 7) Backlog tiep theo (neu can bo sung ky thuat)

- [ ] Them baseline recency/frequency de doi chieu tham khao (khong lam thay doi cot loi de tai).
- [ ] Chuan hoa them 1 runner CLI de tai lap thuc nghiem nhanh.
- [ ] Them smoke-test tu dong cho `test_prediction_metrics` va `run_posthoc_eval` de tranh vo pipeline sau khi sua code.
- [ ] Chot bo bang ket qua theo truc: base AnRe / +improve.md / +tham khao ky thuat tu repo 3 + chuan hoa artifact tu repo 4 + chuan hoa config/test tu repo 5.
