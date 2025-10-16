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
├── src/                     # Core experiment scripts
│   ├── experiment_design.py     # Builds prompts & ground truth
│   ├── run_experiment.py        # Runs LLM queries (manual or API)
│   ├── analyze_bias.py          # Sentiment & keyword analysis
│   ├── validate_claims.py       # Checks LLM statements vs data
│   └── convert_manual_to_jsonl.py  # Converts manual logs for analysis
│
├── prompts/                 # Auto-generated prompt JSONs
├── prompts_for_chat/        # Copy–paste .md prompts for chat UIs
│
├── docs/
│   ├── REPORT.md                # October 15 deliverable report
│   ├── MANUAL_RUN.md            # Instructions for manual Gemini/Claude runs
│   ├── OCT15_PLANNING_SUMMARY.md# Qualtrics-ready planning summary
│   └── All_Prompts_F1.docx      # Combined prompts for copy/paste
│
├── analysis/
│   ├── README.md
│   └── figures/
│
├── data/
│   └── README.md                # No raw data committed (anonymized only)
│
├── results/
│   └── README.md                # Placeholder; real outputs excluded by .gitignore
│
├── config.yaml
├── requirements.txt
├── .gitignore
└── README.md                    # (this file)


---

## 🧪 How to Run (Manual Mode – No APIs)

### Step 1 – Generate Prompts
```bash
python src/experiment_design.py --season 2022 --out prompts
