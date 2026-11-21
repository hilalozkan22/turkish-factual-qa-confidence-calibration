# Dataset card — Turkish Factual QA for Confidence Calibration

## Scope
A Turkish open-ended factual QA dataset covering 13 subject categories and nine answer types. Each record contains a reference answer, accepted aliases and an external source URL.

## Construction and verification
Candidate question-answer pairs were generated with GPT-5.6 (High Thinking) as reported by the researcher. One researcher manually checked factual accuracy, unambiguous answers, temporal stability and accepted aliases against external sources. The supplied final source-review workbook marks all 1,300 records `verified` and `ACCEPT`; 27 study items previously flagged for further review were reportedly checked again. There was no independent second annotator or inter-annotator agreement estimate. The packaging process does not re-fetch or fact-check individual source URLs.

## Experimental splits
- `clean_dev_970.json`: the original 1,000 development questions excluding 30 previously used for model selection.
- `model_selection_30.json`: 30 disjoint questions identified using the recorded Stage 08 model-selection flag.
- `final_test_250.json`: 250 locked independent final-test questions.
- `reserve_50.json`: 50 additional nonexperimental reserve questions.
- `all_experimental_1250.json`: the 1,000 original plus 250 final-test questions.

Test labels are not used to fit the calibrators or select methods. This dataset release does not include generated answers, individual model correctness labels or fitted calibrator weights.

## Provenance and reproducibility
The public JSON values and source register reflect the final manually reviewed Excel workbook, including reviewed answer and alias corrections which the researcher states preceded the calibration experiments. The original immutable 1,250-question dataset was used to recover IDs and membership flags; original question texts are preserved and the final workbook supplies reviewed reference answers, aliases, sources and review status. The initial 1,250 records retain their original `notes`, while reserve records may have empty notes when not supplied by the workbook.

## Limitations
Each record has a source URL but not a copied source passage; a URL does not establish independently verified entailment. Model performance and data quality may differ outside the study's task, model, and temporal context.
