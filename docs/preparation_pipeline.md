# Summary of dataset preparation notebooks 01–02

1. **AI-assisted candidate writing:** Candidate `question`, `reference_answer`, and `accepted_aliases` items were prepared in batches outside notebook 01.
2. **Data checks (Notebook 01):** Validate required fields, nine answer types, aliases, and duplicates; assign `TRQA` identifiers, append accepted batch records and commit versioned raw snapshots.
3. **Validation (Notebook 02 and later review):** Review schema and fingerprints, exact/near duplicates, alias consistency, temporal and ambiguity flags. The researcher reports manually verifying facts and final corrections using an Excel source-review workbook before experiments.
4. **Experiment setup:** Original 1,000-question development collection; 30 prior model-selection questions excluded from Clean-Dev, leaving 970. The 250 final-test questions were fixed before model inference, with 50 additional reserve questions.
5. **Publication:** The source-reviewed workbook supplies the final answers/aliases, external source URLs and review flags; IDs and split membership are cross-checked against the experimental records. There is one published question-answer version, not a separate superseded release.

The supplied notebooks 01/02 are representative of the batch workflow; full model-assisted question-generation chat history and every intermediate notebook version are not included.
