# Bias Detection in LLM Data Narratives, F1 — October 15 Deliverable

## 1. Executive summary (planning plus early signals)
We completed planning and generated prompts, then analyzed your uploaded outputs. Using a lexicon-based proxy, we observe framing effects: negative framing tends to yield lower sentiment than neutral and positive variants. Early summary:
- negative_driver: mean=-0.500 (n=6); neutral_driver: mean=0.333 (n=3); positive_driver: mean=0.667 (n=6); constructor_opps: mean=1.000 (n=3); prime_constructor: mean=0.667 (n=3); neutral_driver_demo: mean=0.000 (n=3)

Demographic and hypothesis-primed variants show shifts in emphasis (e.g., strategy, pit, team) suggesting possible selection and confirmation effects. Full statistical testing will follow in Week 3.

## 2. Methodology
- Dataset: F1 CSVs; 2022 anonymized driver ground truth computed earlier in the project.
- Hypotheses: Framing, demographic, confirmation, selection bias.
- Prompt design: Minimal wording changes across variants; demographic mentions kept generic (nationalities only).
- Collection: Manual copy paste via chat UIs; outputs organized by prompt variant.

## 3. Early results (descriptive)
- Parsed responses: `/mnt/data/Task_08_Bias_Detection_F1/results/responses_parsed_from_docx.csv`
- Sentiment by variant (proxy): `/mnt/data/Task_08_Bias_Detection_F1/analysis/sentiment_by_condition_from_docx.csv`
- Keyword emphasis by variant: `/mnt/data/Task_08_Bias_Detection_F1/analysis/keywords_by_condition_from_docx.csv`

## 4. Next steps
- Finish collecting 3 samples per prompt per model (Gemini 2.5 Pro, Claude Sonnet 4.5, and third model).
- Convert logs to JSONL and run full analysis + numeric validation against ground truth.
- Add figures and statistical tests to the final REPORT.md.

## 5. Ethics & reproducibility
- No PII; anonymized entities.
- Data/results excluded from Git via `.gitignore`.
- Clear manual-run instructions included.

