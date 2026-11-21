# Candidate question generation — provenance limitation

The researcher reports generating candidate Turkish factual QA items with **GPT-5.6 in High Thinking mode**, followed by one-researcher manual verification. The supplied `01_dataset_creation_versioned` notebook ingests already generated JSON batches; it contains data schema/validation/duplicate/versioning code, **not the complete original chat instructions** that generated those batches. Consequently, this release does not claim to reproduce exact question-generation instructions.

The candidate records had fields `question`, `reference_answer`, `accepted_aliases`, `answer_type`, `category`, `source_type`, `source_name`, `source_reference`, `verification_status`, and `notes`. Notebook 01 checked schema, normalized aliases, flagged duplicates, and committed immutable raw snapshots. Notebook 02 performed structural, duplicate, alias and temporal/ambiguity screening, followed by manual source-based acceptance. The scripts evolved over successive batches; these notes describe the provided representative notebooks rather than claiming all historical code snapshots are included.

**If the original GPT-5.6 chat prompt is retrieved, add it as a separate versioned file with its precise provenance.**
