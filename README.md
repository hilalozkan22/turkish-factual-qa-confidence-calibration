# Turkish Factual QA for Confidence Calibration (MIDI 2026)

Dataset and recorded model-response/confidence prompts accompanying *When Should We Trust Language Models? On Confidence Calibration in Turkish Question Answering* (MIDI 2026).

This release provides **1,300 source-reviewed Turkish factual QA questions**, including the **1,250 questions in the experimental protocol** (1,000 development/model-selection plus 250 locked final-test questions), **50 reserve questions**, question-level source URLs, and recorded inference prompts.

## Dataset organization

| File | Items | Use |
|---|---:|---|
| `data/clean_dev_970.json` | 970 | Calibration development questions (excluding the 30 model-selection questions) |
| `data/model_selection_30.json` | 30 | Questions excluded from calibration fitting because they were used for prior model selection |
| `data/final_test_250.json` | 250 | Locked independent final test questions |
| `data/reserve_50.json` | 50 | Not used in the reported experiments |
| `data/all_experimental_1250.json` | 1,250 | 1,000 original questions plus 250 final-test questions |
| `data/source_register_1300.csv` | 1,300 | Source URLs, verification flags, split membership |
| `data/split_ids.json` | 1,300 IDs | Explicit immutable split lists |
| `data/record_schema.json` | — | Schema and vocabulary |
| `data/release_manifest.json` | — | Provenance, split sizes and file checksums |

**Important:** The original 1,000 development questions include the 30 prior model-selection questions. The remaining **970** belong to Clean-Dev. The 250 independent final-test questions are disjoint from development; 50 reserve questions are not part of the original 1,250 experimental records.

## Prompt and configuration files

See [`prompts/README.md`](prompts/README.md) and `prompts/primary_answer.json`, `prompts/self_confidence.json`, `prompts/self_verification.json`, and `prompts/self_consistency.json`. The generation settings are in `configs/generation_settings.json`.

Question candidate generation with GPT-5.6 High Thinking was conducted interactively as reported by the researcher. The complete verbatim question-generation conversation prompt was **not** preserved in the supplied dataset-management notebooks; see `prompts/question_generation_provenance.md`. Do not confuse inference prompts with question-generation prompts.

## Research notebooks: workflow documentation

The `notebooks/` directory contains **20 historical research notebooks (Stages 01–20)**, shared to document the broad progression from dataset preparation and model selection through confidence-feature extraction, calibration, evaluation, and additional MIDI 2026 analyses. They are provided **for methodological transparency and reference**, not as a validated, end-to-end reproduction pipeline.

These notebooks were developed and revised at different stages of the research. Some may differ from the exact code or execution state used to obtain the paper's final numbers. They may rely on Google Colab, external model downloads, hardware-specific runtimes, personal Google Drive directory layouts, or intermediate artifacts that are **not included** in this repository. **Successful execution in sequence, exact numerical reproduction, and regeneration of all published figures are not guaranteed.** No end-to-end rerun of the complete notebook collection was performed for this release.

The **primary release materials are the reviewed dataset and its documented splits (`data/`), the recorded response/confidence prompts (`prompts/`), and generation/model configurations (`configs/`)**. The notebook files provide supporting research context.

## Verification provenance

A single researcher reports manually verifying questions, references, and aliases against external sources **before the calibration experiments**, including source-review corrections. The supplied final review workbook marks all 1,300 records as `verified` / `ACCEPT`. This release uses the final reviewed workbook's answers and aliases rather than separately publishing a superseded prior version. We have not independently verified the chronology of corrections or rechecked the accuracy of each source link.

For field definitions and limitations, see [`docs/dataset_card.md`](docs/dataset_card.md). For the dataset preparation workflow, see [`docs/preparation_pipeline.md`](docs/preparation_pipeline.md).

## Reproducibility and versioning

Run the offline consistency check:

```bash
python scripts/verify_release.py
```

The script checks exact split sizes, unique IDs, disjoint partitions, source-register consistency, and SHA-256 integrity. It does **not** recompute model confidence scores or independently verify the paper's reported Brier/ECE/AUROC/AURC values. Reproducing the numerical results requires the corresponding model predictions, correctness labels, and evaluation configuration. The source workbook contains historical `record_fingerprint` metadata, which may not reflect subsequent manual verification updates. Integrity checks for this public release therefore rely on the final source-register values and file checksums.


## Citation and License

If you use this dataset or its accompanying materials
in your research, please cite the associated MIDI 2026
paper and the dataset release.

The dataset (`data/`), prompts (`prompts/`),
configuration files (`configs/`), and documentation
(`docs/`) are licensed under Creative Commons
Attribution 4.0 International (CC BY 4.0).

The Python verification code in `scripts/` and the historical research
notebooks in `notebooks/` are licensed separately under the MIT License.
Each directory contains its own `LICENSE` file.

These licenses apply only to material for which the
repository authors hold the necessary rights.
Linked third-party source materials retain their
respective rights and licenses.

Citation metadata is provided in `CITATION.cff`.

