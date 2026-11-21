# Exact LLM response and confidence elicitation prompts

The files in this directory reproduce the **exact text** of the system messages and the user-message templates from experimental notebooks 04–06. `{question}` and `{answer}` are placeholders, not literal example content. JSON `\n` sequences represent the original line breaks. The primary-answer and self-consistency stages share the same system prompt. The target-model-specific chat template is applied by the original Hugging Face tokenizer/processor.

| File | Purpose | Input placeholders |
|---|---|---|
| `primary_answer.json` | Primary Turkish factual answer | `question` |
| `self_confidence.json` | Self-rating on a 0–100 scale | `question`, `answer` |
| `self_verification.json` | A/B/C classification; next-token probabilities form the confidence feature | `question`, `answer` |
| `self_consistency.json` | Five stochastic responses to the primary-answer task | `question` |

**Question candidate generation is separate.** Dataset creation notebook 01 manages AI-generated batches but does not contain the exact interactive GPT-5.6 High Thinking instructions. We do not substitute a fabricated prompt: see `question_generation_provenance.md`.
