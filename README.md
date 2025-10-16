# Task_08_Bias_Detection

# 🏎️ Task 08 – Bias Detection in LLM Data Narratives (F1 Dataset)

This repository implements a controlled experiment to detect **biases in Large Language Model (LLM)**–generated data narratives.  
It follows the structure of **Research Task 08** (Bias Detection in LLM Data Narratives) under Syracuse University’s research framework.

---

## 📘 Objective
To test whether identical datasets produce **different analyses from LLMs** when the **prompt framing** or **demographic context** changes.  
The experiment investigates:
- **Framing Bias:** “underperforming” vs “developing”
- **Demographic Bias:** inclusion of nationalities or protected traits
- **Confirmation Bias:** testing primed hypotheses (e.g., “Ferrari has the strongest strategy”)
- **Selection Bias:** which statistics the model emphasizes (wins, DNFs, pit stops, etc.)

---

## 🧩 Dataset
We use anonymized Formula 1 performance data from the **2022 season**, derived from:
- `drivers.csv`, `races.csv`, `driver_standings.csv`, `pit_stops.csv`, and related files  
- Each driver anonymized as **Driver A, Driver B, Driver C**, etc.

The ground truth file is automatically generated as: analysis/ground_truth_drivers_2022.csv

---

## 🧠 Hypotheses
| ID | Hypothesis | Bias Type |
|----|-------------|-----------|
| H1 | LLM recommendations differ when describing a driver as “struggling” vs “developing.” | Framing |
| H2 | Mentioning driver nationality changes which driver is recommended for improvement. | Demographic |
| H3 | Asking “what went wrong” vs “what opportunities exist” alters conclusions. | Framing |
| H4 | Priming with “Ferrari has the strongest strategy” increases model agreement. | Confirmation |
| H5 | Different phrasings shift which stats the model emphasizes. | Selection |

---

## ⚙️ Repository Structure

Task_08_Bias_Detection_F1/
│
├── 📁 src/                          # Core experiment scripts
│   ├── experiment_design.py         # Builds anonymized F1 dataset & generates prompt sets
│   ├── run_experiment.py            # Runs or simulates LLM outputs (manual/API)
│   ├── analyze_bias.py              # Sentiment & keyword-based bias analysis
│   ├── validate_claims.py           # Compares model statements to ground truth data
│   └── convert_manual_to_jsonl.py   # Converts manual chat logs (CSV) → JSONL
│
├── 📁 prompts/                      # JSON prompts for each bias condition
│   ├── prompts_neutral_driver.json
│   ├── prompts_positive_driver.json
│   ├── prompts_negative_driver.json
│   ├── prompts_neutral_driver_demo.json
│   ├── prompts_positive_driver_demo.json
│   ├── prompts_negative_driver_demo.json
│   └── prompts_prime_constructor.json
│
├── 📁 prompts_for_chat/             # Copy–paste-ready .md prompt files for Gemini & Claude
│   ├── neutral_driver.md
│   ├── negative_driver.md
│   ├── positive_driver.md
│   ├── prime_constructor.md
│   └── *_demo.md
│
├── 📁 docs/                         # Reports & research documentation
│   ├── REPORT.md                    # October 15 deliverable (executive summary & plan)
│   ├── MANUAL_RUN.md                # Instructions for running via Gemini / Claude chat
│   ├── OCT15_PLANNING_SUMMARY.md    # Qualtrics-ready summary for OPT reporting
│   ├── All_Prompts_F1.docx          # All prompts combined for quick copy-paste
│   └── README.md                    # (Optional) extra project notes
│
├── 📁 analysis/                     # Analytical outputs
│   ├── ground_truth_drivers_2022.csv # Computed driver stats (points, pits, perf_score)
│   ├── sentiment_by_condition_from_docx.csv
│   ├── keywords_by_condition_from_docx.csv
│   ├── validation_summary.csv
│   └── 📁 figures/                  # Auto-generated visualizations
│
├── 📁 data/                         # Raw CSVs (excluded from GitHub)
│   ├── README.md                    # Placeholder; actual CSVs not committed
│
├── 📁 results/                      # Model responses (excluded from GitHub)
│   ├── manual_log_template.csv      # Template to record Gemini/Claude outputs
│   └── README.md
│
├── config.yaml                      # Config file for reproducibility
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Prevents committing raw data/results
├── .github/workflows/lint.yml       # Optional CI workflow for linting
└── README.md                        # Project overview & usage guide
---

## 🧪 How to Run (Manual Mode – No APIs)

### Step 1 – Generate Prompts
```bash
python src/experiment_design.py --season 2022 --out prompts
